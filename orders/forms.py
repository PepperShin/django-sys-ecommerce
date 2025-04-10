from django import forms
from orders.models import ShippingAddress


# dev_25
class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all__"  # 모든 필드를 인풋 태그로 변환
        exclude = ["user", "order"]  # foreign키는 제외. dev_26_2 order 추가
