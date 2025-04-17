from rest_framework.decorators import api_view
from store.models import Category
from api.serializers.category_serializers import CategorySerializer
from rest_framework.response import Response


# dev_32
@api_view(["GET"])
def categories_api(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
