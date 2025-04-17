from rest_framework import serializers
from store.models import Category, Product


# dev_34
# nested 전용 시리얼 라이저
class ProductSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    from api.serializers.category_serializers import CategorySimpleSerializer

    category = CategorySimpleSerializer()

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category_data = validated_data.pop("category")

        # 카테고리 저장/조회
        category, _ = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(**validated_data, category=category)

        return product
