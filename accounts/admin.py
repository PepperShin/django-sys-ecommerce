from django.contrib import admin
from accounts.models import User

# Register your models here.
# dev_9
# 1. 기본적인 관리자 페이지에서 기본적인 등록
admin.site.register(User)
