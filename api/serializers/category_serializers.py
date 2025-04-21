from rest_framework import serializers
from store.models import Category, Product


# dev_34
# nested 전용 시리얼 라이저
class CategorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    from api.serializers.product_serializers import ProductSimpleSerializer

    product = ProductSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = "__all__"
