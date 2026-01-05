from django import forms  # ModelForm이라는 class가 있음
from .models import Article
# Model이 어떻게 정의되어있는지 확인하고 거기에 어울리는 html을 자동으로 만들어줌
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'