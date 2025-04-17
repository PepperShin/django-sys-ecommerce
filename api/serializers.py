from rest_framework import serializers
from store.models import Category, Product

# Serilaizer 객체의 주요 기능
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


# dev_32
class CategorySerializer(serializers.ModelSerializer):
    # product = ProductSerializer(
    #     many=True, read_only=True
    # )  # 역방향 참조 category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")

    class Meta:
        model = Category
        fields = "__all__"


# dev_33
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True
    )  # dev_33_2 read_only를 안하면 False가 기본

    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id", "name", "price"]
        # dev_32
        # depth = 1  # ForeignKey 필드 자동 직렬화

    # dev_31
    # 0 이상 10,000 이하만 들어가게 하겠다.
    # def validate_price(self, value):
    #     if value < 0:
    #         raise serializers.ValidationError("가격은 0 이상이어야 합니다.")

    #     if value > 100000:
    #         raise serializers.ValidationError("가격은 100000 이하여야 합니다.")

    #     return value

    # # 이름은 3자 이상 100자 이하
    # def validate_name(self, value):
    #     if len(value.strip()) < 3:  # 문자열 양끝 공백 제거
    #         raise serializers.ValidationError("상품 이름은 최소 3자 이상이어야 합니다.")

    #     if len(value.strip()) > 100:
    #         raise serializers.ValidationError("상품 이름은 100자를 초과할 수 없습니다.")

    #     return value

    # # 함수 오버라이드
    # def validate(self, data):
    #     is_sale = data.get("is_sale")  # 딕셔너리 문법
    #     sale_price = data.get("sale_price")

    #     if is_sale:
    #         # 세일중이면 sale_price는 반드시 필요하고 0보다 커야 함
    #         if sale_price is None or sale_price <= 0:
    #             raise serializers.ValidationError(
    #                 {"sale_price": "sale_price는 0보다 커야 합니다."}
    #             )

    #     else:
    #         # 세일이 아니면 sale_price는 아예 없어야 함(자동 무시하거나 경고)
    #         if sale_price and sale_price > 0:
    #             raise serializers.ValidationError(
    #                 {
    #                     "sale_price": "is_sale이 false 이면 sale_price를 지정할 수 없습니다."
    #                 }
    #             )

    #     return data

    # dev_33
    # def create(self, validated_data):
    #     category_data = validated_data.pop(
    #         "category"
    #     )  # pop을 해서 카테고리 부분을 떼어낸다.

    #     # 카테고리 저장 및 조회
    #     category, _ = Category.objects.get_or_create(
    #         **category_data
    #     )  # 카테고리 객체와 뒤에는 시간.
    #     product = Product.objects.create(**validated_data, category=category)

    #     return product

    # {
    #     "id": 1,
    #     "name": "명품자바",
    #     "price": "12000.00",
    #     "description": "자바 책입니다.",
    #     "image": "/media/upload/product/%EB%AA%85%ED%92%88%EC%9E%90%EB%B0%94_b9raYG9.jpg",
    #     "is_sale": false,
    #     "sale_price": 10000
    # },

    # "category": {
    #     "id": 2,
    #     "name": "자바"
    # },
