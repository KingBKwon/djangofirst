from rest_framework import serializers
from .models import BOOK

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model=BOOK
    #클라이언트에서 입력하는 데이터만 나열
    #아래 나열한 데이터를 입력하면 Book 클래스의 인스턴스 생성
    fields=['bid','title','author','publishdate','existence']
    