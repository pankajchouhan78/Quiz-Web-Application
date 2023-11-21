from django.shortcuts import render, redirect
from .forms import CreateUserForm, AddQuestionFrom
from django.contrib.auth import authenticate, login, logout
from .models import Question

# Create your views here.
def home(request):
    if request.method == "POST":
        questions = Question.objects.all()
        score=0
        correct=0 
        wrong=0
        total=0
        for que in questions:
            total+=1
            ans = request.POST.get(que.question)

            # print(que.answer)
            # print(ans)
            
            if que.answer == ans:
                score+=10
                correct+=1
            else:
                print("enter else block me")
                wrong+=1

        percent = score/(total*10) * 100
        context={
            'score':score,
            'time':request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, "result.html",context)
    
    else:
        questions = Question.objects.all()
        context ={
            "questions":questions,
        }
        return render(request, "home.html", context)


def add_question(request):
    if request.user.is_staff:
        form = AddQuestionFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {
            'form':form,
        }
        return render(request, "add_question.html", context)
    else:
        return redirect('/home/')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        context = {
            'form':form
        }
        return render(request,"register.html",context)
    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
        return render(request, "login.html")
    
def logout_user(request):
    logout(request)
    return redirect('/')
