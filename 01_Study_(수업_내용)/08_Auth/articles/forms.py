from django import forms
from .models import Article, Comment

# http://127.0.0.1:8000/articles/create/ 홈페이지를 보여주는 부분
    # 2교시 25분
class ArticleForm(forms.ModelForm):

    # 첫번째 방법 4교시 7분쯤 부터 내용 강제로 넣는 방식
    # title = forms.CharField(
    #     label = '제목 입니다.'
    #     wiget=forms.TextInput() # text를 위한 input을 넣어주세요
    #         attrs={'class':'form-control'}
    # )
    # # content = 

    class Meta:
        model = Article
        #fields = '__all__'
        
        #fields = ('title', 'content')
        # 위, 아래 출력해 주는 내용은 같음
        exclude = ('user', )
       
       
        # widget = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('content', )

