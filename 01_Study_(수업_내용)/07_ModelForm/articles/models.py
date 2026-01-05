from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # add 할 때만
    update_at = models.DateTimeField(auto_now = True) # 수정할 때마다