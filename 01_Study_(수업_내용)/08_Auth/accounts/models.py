from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): # AbstractUser에 있는 기능을 다 User에 넣어 준다. 이름만 User로 바꾸어서 쓰는것
    pass
    # article_set = 
    # 1교시 25분 쯤
    # comment_set
    # article/models.py의 line 42번 Foreignkey 를 이용해서 1 대 N으로 연결


# migration 을 하기 미리 model을 정하는게 좋다, 그 이유는 프로젝트를 진행하면서 중간에 변경하기에는 위험 하기 때문에   
