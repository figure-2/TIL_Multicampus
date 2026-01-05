from django.urls import path
from . import views

app_name = 'balance'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:question_id>/', views.index, name='index'),
    path('<int:question_id>/answer_click', views.answer_click, name = 'answer_click'),
    path('create/', views.create, name = 'create'),
    path('settings/', views.settings, name='settings'),
]