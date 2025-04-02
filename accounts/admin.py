from django.contrib import admin
from accounts.models import User

# Register your models here.
# dev_9
# 1. 기본적인 관리자 페이지에서 기본적인 등록
# admin.site.register(User)

# dev_12
"""
어드민 페이지 등록방법 3가지

1. 기본적인 관리자 페이지에서 기본적인 등록
    admin.site.register(User)
    커스텀 기능 (검색, 필터, 필드 설정 등)을 추가할 수 없다.

2. ModelAdmin 클래스를 활용하는 방법(커스텀 기능)
    class UserAccountsAdmin(admin.ModelAdmin):
        list_display=[
            "username",
            "email",
            "job",
            "gender",
        ]

        search_fields = [
            "username",
            "email",
            "job",
            "gender",
        ]

        list_filter = (
            "username",
            "email",
            "job",
            "gender",
        )
        
    admin.site.register(User, UserAccountsAdmin)
    검색은 db 저장되는 값으로 검색 가능
    튜플이나 리스트 둘 다 사용 가능

3. @admin.register(User, UserAccountsAdmin) 데코레이터 사용
    @admin.register(User)
    class UserAccountsAdmin(admin.ModelAdmin):
        list_display = [
            "username",
            "email",
            "job",
            "gender",
        ]

        search_fields = [
            "username",
            "email",
            "job",
            "gender",
        ]

        list_filter = (
            "username",
            "email",
            "job",
            "gender",
        )
"""


@admin.register(User)
class UserAccountsAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "job",
        "gender",
    ]

    search_fields = [
        "username",
        "email",
        "job",
        "gender",
    ]

    list_filter = (
        "username",
        "email",
        "job",
        "gender",
    )
