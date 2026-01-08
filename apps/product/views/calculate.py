from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.product.models import Product, ProductMaterial, Warehouse
from apps.product.serializers.calculate import CalculateSerializer


class CalculateView(APIView):

    def post(self, request):
        serializer = CalculateSerializer(data=request.data, many=True)

        serializer.is_valid(raise_exception=True)
        items = serializer.validated_data

        warehouses = Warehouse.objects.all().order_by('id')

        virtual_remainders = {
            w.id: w.remainder for w in warehouses
        }

        result = []

        for item in items:
            product_code = item["code"]
            product_qty = item["quantity"]

            product = Product.objects.get(code=product_code)

            product_materials = []

            for pm in ProductMaterial.objects.filter(product=product):
                needed_qty = pm.quantity * product_qty

                material_warehouses = warehouses.filter(
                    material_id=pm.material_id
                )

                if not material_warehouses.exists():
                    product_materials.append({
                        "warehouse_id": None,
                        "material_name": pm.material.name,
                        "qty": needed_qty,
                        "price": None
                    })
                    continue

                for wh in material_warehouses:
                    if needed_qty <= 0:
                        break

                    available = virtual_remainders.get(wh.id, 0)
                    take = min(available, needed_qty)

                    if take > 0:
                        product_materials.append({
                            "warehouse_id": wh.id,
                            "material_name": pm.material.name,
                            "qty": take,
                            "price": wh.price
                        })

                        virtual_remainders[wh.id] -= take
                        needed_qty -= take

                if needed_qty > 0:
                    product_materials.append({
                        "warehouse_id": None,
                        "material_name": pm.material.name,
                        "qty": needed_qty,
                        "price": None
                    })

            result.append({
                "product_name": product.name,
                "product_qty": product_qty,
                "product_materials": product_materials
            })

        return Response(
            {"result": result},
            status=status.HTTP_200_OK
        )
