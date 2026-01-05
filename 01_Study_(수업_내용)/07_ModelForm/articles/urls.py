from django.urls import path
from . import views

app_name = 'articles'

urlpatterns =[
    path('', views.index, name = 'index'), # modelFrom의 urls가 합쳐지는거니 '' => 'articles/'라는 의미임
    path('<int:id>/', views.detail, name = "detail"),
    
    path('create/', views.create, name = 'create'),

    path('<int:id>/delete/', views.delete, name = 'delete'),

    path('<int:id>/update', views.update, name = "update"),
]