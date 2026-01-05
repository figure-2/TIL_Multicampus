from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles  # key값에 article로 하게될 경우 index.html에서 for문이 돌지 않음 주의!!
    }

    return render(request,'index.html',context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article' : article
    }
    return render(request, 'detail.html', context)

def create(request):
    # POST요청 : 사용자가 입력한 데이터를 DB에 저장
    # create 기능
    if request.method == 'POST':
        form = ArticleForm(request.POST)  # 전엔 title = request.POST.get('title') 하나씩 다 가져와야했음 하지만 modelform으로 컬럼이 몇개든 자동으로 데이터를 집어넣음
        
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        else:
            form = ArticleForm()

            context ={
                'form' : form,
            }
            return render(request, 'create.html', context)
    # GET요청 : 사용자가 데이터를 입력할 수 있도록 빈 종이(form)을 리턴
    # new에 해당하는 기능
    else:
        form = ArticleForm()

        context = {
            'form' : form,
        }
        return render(request, 'create.html', context)
    
def delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')

def update(requset,id):
    article = Article.objects.get(id=id) # 기존 정보
    # POST
    if requset.method == "POST":
        form = ArticleForm(requset.POST, instance=article)
        
        if form.is_valid():  # 정보 유효하냐?
            form.save() # article = form.save()
            return redirect('articles:detail', id=id) # return redirect('articles:detail', id=article.id)
    # GET
    else:
        form = ArticleForm(instance=article) # form = ArticleForm()빈종이/ form = ArticleForm(instance=article) 기존 정보 작성

    context = {
        'form' : form,
    }
    return render(requset,'update.html',context)
    