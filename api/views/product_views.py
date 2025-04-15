from rest_framework.decorators import api_view
from store.models import Product
from api.serializers import ProductSerializer
from rest_framework.response import Response


# dev_29
@api_view(["GET"])
def products_api(request):
    if request.method == "GET":
        products = Product.objects.all()
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
