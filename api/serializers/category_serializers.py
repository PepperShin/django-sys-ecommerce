from rest_framework import serializers
from store.models import Category, Product
from api.serializers.product_serializers import ProductSimpleSerializer


# dev_34
# nested 전용 시리얼 라이저
class CategorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):

    products = ProductSimpleSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"
