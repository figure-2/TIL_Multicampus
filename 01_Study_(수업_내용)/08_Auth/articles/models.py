from django.db import models
from accounts.models import User
# accounts의 model.py 와 연동해서 사용하기 위해서 연결
from django.conf import settings
# auth/settings.py line 128d에 있는 settings.AUTH_USER_MODEL을 쓰기 위해 연동
from django.contrib.auth import get_user_model

# Create your models here.
# 로그인 했을때 게시글을 쓰거나 댓글을 쓸 수 있는 기능을 만들어 준다


class Article(models.Model): # 게시물 쓰는 기능
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set -> 장고가 자동으로 추가해주는 칼럼

    # # # 유저 모델을 참조하는 경우
    # # # 방법. 1 (권장하지 않음)

    # # user = models.ForeignKet(User, on_delete=models.CASCADE)
    # # # line 2에서 연동한 User를 불러와서 사용

    # # 방법. 2 (권장)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # # auth/settings.py line 128d에 있는 settings.AUTH_USER_MODEL을 가져와서 사용
    # # settings.AUTH_USER_MODEL에는 account.User가 들어가있다

    
    # 방법. 3 (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model): # 댓글 다는 기능
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # 1 대 N 관계를 설정
    # Article 이라는 객채를 가지게 됨

    # article_id -> 장고가 자동으로 추가해주는 칼럼

    # 위에 3번째와 같은 방법
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id = 