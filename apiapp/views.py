from rest_framework.response import Response
from rest_framework.decorators import api_view

#python에서 @으로 시작하는 단어는 decorator라 하는데
#실제함수를 호출하면 특정내용을 삽입해서 함수를 실행
#반복적으로 사용하는 내용이나 직접 작성하기 번거로운 내용을
#decorator 라고 만듭니다
#GET 요청이 오면 함수 호출
@api_view(['GET']) 

def hello(request):
  return Response("Hello Rest API")


from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import BOOK
from .serializers import BookSerializer

#get과 포스트 모두를 처리
@api_view(['GET','POST'])
def booksAPI(request):
  #조회(GET)을 요청
  if request.method =='GET':
    #테이블의 데이터를 전부 가져오기
    books=BOOK.objects.all()
    #출력하기 위해서 브라우저의 형식으로 데이터 변환
    serializer=BookSerializer(books,many=True)
    #출력
    return Response(serializer.data)
    
  #유효성 검사를 수행해서 통과하면 삽입하고 그렇지 않으면
  #실패한 이유를 출력합니다
  #POST 방식의 처리 -삽입하는 경우
  elif request.method =="POST":
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
    
  