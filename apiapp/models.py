from django.db import models

# Create your models here.
#apiapp_book이라는 테이블을 생성
class BOOK(models.Model):
  bid =models.IntegerField(primary_key=True)
  title=models.CharField(max_length=50)
  author=models.CharField(max_length=50)
  publishdate=models.DateField()
  existence=models.BooleanField()
  