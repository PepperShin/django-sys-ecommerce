from rest_framework import serializers
from store.models import Category, Product

# 2. Serilaizer 객체의 주요 기능
# serialization
# deserialiaztion
# validation
# request / response 데이터 핸들링 ( to_internal_value() / to_representation() )
# nested serialization


# dev_29 Product model을 시리얼라이즈
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.ImageField()
#     # Foreign 키
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     description = serializers.CharField(
#         max_length=250, required=False, allow_blank=True, allow_null=True
#     )
#     image = serializers.ImageField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "price"]
