from django.contrib import admin
from .models import Post  # 같은 폴더에 있는 다른 모델을 참조할 때 .models

# Register your models here.
admin.site.register(Post)
