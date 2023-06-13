from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    # 최대 20자까지 글자수를 정함
    content = models.TextField()
    # 글자수 제한없이 할 수 있는 textfield