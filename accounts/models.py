from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# dev_9
# User 계정 커스터마이징 방법은 4가지 정도가 있다.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    gender = models.CharField(
        verbose_name="성별",  # Admin 페이지에서 성별로 표시
        max_length=1,  # 글자 길이 하나
        choices=GenderChoices.choices,  # DB에는 M, F만 들어가고 Admin 페이지에서는 남성 여성으로 표시.
    )

    JOBS = (
        ("P", "교수/강사(Professor/Lecturer)"),
        ("S", "학생(Student)"),
        ("R", "연구원(Researcher)"),
        ("E", "기타(Etc.)"),
    )

    job = models.CharField(
        verbose_name="직업",
        max_length=1,
        choices=JOBS,  # 튜플 형식으로도 지정할 수 있다.
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # dev_23
    old_cart = models.CharField(max_length=1000, blank=True, null=True)
