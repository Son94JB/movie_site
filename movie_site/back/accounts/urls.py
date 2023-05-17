from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<user_id:int>/', views.profile),  # 유저 프로필로 가자
    path('login/', views.login),  # 로그인 데이터를 받아서 확인하자
    path('signup/', views.signup),  # 회원가입 데이터를 받아서 DB에 저장을 하자
    # path('movies/', include('movies.urls'))
]
