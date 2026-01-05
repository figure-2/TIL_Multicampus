from django.shortcuts import render,redirect
from .models import Question
from .forms import AnswerForm, QuestionForm
import random

# Create your views here.
def main(request):
    return render(request,'main.html')

def index(request, question_id):
    question = Question.objects.get(id=question_id)

    # for question in question.answer_set.all():
    click_all = len(question.answer_set.all())+0.1
    choice_A = question.answer_set.all().filter(click='a')
    choice_B = question.answer_set.all().filter(click='b')

    choice_A_percent = int(len(choice_A)/click_all * 100)
    choice_B_percent = int(len(choice_B)/click_all * 100)


    context = {
        'question' : question,
        'choice_A' : choice_A,
        'choice_B' : choice_B,
        'choice_A_percent' : choice_A_percent,
        'choice_B_percent' : choice_B_percent,
    }
    return render(request, 'index.html', context)


def answer_click(request, question_id):
    # question = Question.objects.get(id=question_id)
    answer_form = AnswerForm()

    answer = answer_form.save(commit=False)

    answer.question_id = question_id    
    answer.click = (request.GET.get('choice'))
    answer.save()

    question_len = len(Question.objects.all())
    question_id = random.choice(range(1,question_len))
    return redirect('balance:index', question_id)

def create(request): 

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # article = form.save(commit = False) # DB로는 아직 넣지 말고 객체에만 넣고 멈춰 ( request에 들어간 정보는 title, content )
            # article.user = request.user # (마지막으로 user도 채움) => 채운것에 대한 기준은 Article 모델에 들어간 객체들이 들어가야함.
            form.save() # 모든 컬럼에 대해서 정보 채워넣었으니 저장
            return redirect('balance:index', question_id = 1)

    else:
        form = QuestionForm()

    context = {
        'form' : form
    }
    return render(request, 'form.html', context)


def settings(request):
    questions = Question.objects.all()

    context = {
        'questions' : questions,
    }

    return render(request,'setting.html',context)

def delete(request,question_id):
    question = Question.objects.get(id=question_id)
    question.delete()

    return redirect('balance:settings')