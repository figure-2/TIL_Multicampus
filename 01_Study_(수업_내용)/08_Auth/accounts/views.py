from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm 
# .forms라는 파일에서 CustomUserCreationForm 을 불러온다.
from django.contrib.auth import login as auth_login
# 30번째 라인에 내가 만들어줌 함수 정의 (def)에 login 과 django에서 불러온 login의 이름이 같아서 문제가 발생
# 그 이유는 LEGV 가장 가까운 변수를 먼저 찾기 때문에 내가 만들어줌 함수 이름에 접근을 해서 재귀함수가 되면서
# 문제가 발생된다
# 위와 같은 문제를 해결하기 위해서 "as"를 이용해서 이름(변수)을 바꾸어준다.
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 로그인 이미 한 사람이 로그인을 누르면 들어오지 못하게 막아주는 기능


     # request.method 가 POST방식인지 아닌지 확인
    if request.method == 'POST': # POST방식를 통해 데이터가 들어왔을때 저장해줌
        form = CustomUserCreationForm(request.POST) # signup.html에서 POST를 통해 받음
        if form.is_valid(): # 검증 후에
           #form.save() # form에 저장
           user = form.save() 
           # print(user, user.username, user.password)
           # user에는 user에 대한 인스턴스가 들어간다.
           # accounts/model.py의 class --로 만들어진 user 정보?
           auth_login(request, user)
           return redirect('articles:index')
            #return redirect('accounts:signup') # signup 에 계정 정보를 보내준다?


    else: # 사용자가 GET방식으로 요청을 한것이 때문에 빈 종이를 보내줌 
          # model form을 이용해서 빈종이를 만든다. -> accounts 에 forms을 만들어줘야한다.
        form = CustomUserCreationForm() # form에 CustomUserCreationForm을 instance한다
# instance 란 객체를 소프트웨어에 실체화 하는것이며 실체화된 instance는 메모리에 할당
    context = {
        'form': form,
    }
    # 'form' 에다가 form을 넣고 context에 담아준다

    return render(request, 'account_form.html', context) # signup.html 이라는 공간에 보내준다.

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 로그인 이미 한 사람이 로그인을 누르면 들어오지 못하게 막아주는 기능
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) 
# 이것도 django 에 있는것을 사용 하며 Authentication은 만들어질때 부터 (request, request.POST)을 사용하라고 함
# Authentication 안에다가 request.POST를 넣으면 비밀번호를 검증한다.
        if form.is_valid():
            auth_login(request, form.get_user()) 
          # http://127.0.0.1:8000/accounts/login/?next=/articles/create/
# 첫번째 인자는 request 두번째 form.get_user() 라는 넣어서 실행한다.
# form.get_user()를 하면 user에 대한 정보에서 일치하는 유저에 찾아 객체를 보내준다
            next_url = request.GET.get('next') 
            # /articles/create/
            # return redirect('accounts:login')
            return redirect(next_url or 'articles:index')
            # next 인자가 url에 있을 때 -> '/articles/create/' or 'articles:index'
            # or의 역활은 둘중에 하나라도 T면 T를 출력 
            # 즉 앞에 '/articles/create/이 T면 뒤'articles:index' 와 상관 없이 T를 출력
            # 둘다 F면 F를 출력.
            # next 인자가 url에 없을 때   -> None or 'article:index'  
            # 앞에 값이 없으면 뒤에 'article:index' 값을 사용한다.     

# 3-23 부분 추가 공부

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'account_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
