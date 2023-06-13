from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 변경하기 쉽게 custom으로 만든다.
class User(AbstractUser):
    pass
    # 등급 등 유저의 추가적인 속성을 기록할 수 있음