
from django.contrib import admin
from django.urls import path
#url의 처리를 다른 모듈에게 위임하고 할 때 사용하는 패키지 import
from django.urls import include


#    path("example/",include("appiapp.urls")),
#위 문장은 example로 시작하는 요청이 오면 apiapp 애플리케이션 urls.py 파일에 처리 위임


urlpatterns = [
    path("admin/", admin.site.urls),
    path("example/",include("apiapp.urls")),
]
