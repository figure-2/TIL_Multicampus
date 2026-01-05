from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    articles = Article.objects.all()
    # 전체 게시글을 조회
    form = CommentForm()

    context = {
        'articles': articles,
        'form': form,
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    # if not request.user_authenticated:
    #     return redirect('accounts:login')
    # # 로그인하지 않고 url을 직접 입력해서 게시글을 쓸려고 하는것을 막기
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
#             form.save()
# # form.save() 를 하면 문제가 발생함. why? articles/model.py에서 
# title, content, user에 대한 정보를 
# 2교시 38분 부분
            article = form.save(commit=False)
            article.user = request.user
            # 현제 로그인한 사람이 넣은 정보를 입력한다.
            article.save
            return redirect('articles:index')

    else: 
# get 요청이 먼저 와서 else 부터 실행 하며 articles/ forms.py 생성해서 
# 인스턴스해준다 line 3 부분
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


@login_required # 로그인 하지 않은 사람들에게는 안보여지게 하는것
def comment_create(request, article_id):
    article = Article.objects.get(id=article_id)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        # 로그인한 사람 정보
        comment.article = article # 51번에 있는 article을 가져옴
        comment.save()

        return redirect('articles:index')
