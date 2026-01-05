from django.urls import path
from . import views  # 둘 다 posts라는 경로에 있기 때문에 .으로 표기

app_name = 'posts' # 변수설정(urls 모아놓은 이름공간) url을 변수로 설정(app_name + name)

urlpatterns = [
    # Read
    path('',views.index, name = 'index'),
    path('<int:id>/',views.detail,name='detail'),

    # Create
    path('new/', views.new, name='new'),
    path('create/',views.create, name = 'create'),

    # Delete
    path('<int:id>/delete/',views.delete,name="delete"),

    # Update
    path('<int:id>/edit/', views.edit, name="edit"),
    path('<int:id>/update/', views.update, name = "update"),
]
