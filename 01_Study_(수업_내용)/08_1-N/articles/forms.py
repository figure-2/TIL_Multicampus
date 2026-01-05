from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'  # 전체 컬럼 다 출력


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'  article 빼야하기 때문에 __all__ (x)

        # fields => 추가할 필드 이름 목록
        # exclude => 제외할 필드 이름 목록
        
        # exclude = ('article', )
        fields = ('content', )