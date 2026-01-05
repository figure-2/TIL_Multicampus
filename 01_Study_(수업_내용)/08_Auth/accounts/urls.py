from django.urls import path # django.urls에 있는 path 함수를 불러온다
from . import views # . 해당 폴더에서 views를 불러온다

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), #  signup에 대한 경로를 잡음
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
