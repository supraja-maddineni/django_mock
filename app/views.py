from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from app.models import *
class QuestionList(ListView):
    model= Question
    context_object_name='que'
    template_name='app/home.html'

class QuestionDeatil(DetailView):
    model=Question
    context_object_name='qobj'
    template_name='app/quesion_detail.html'

# Create your views here.
from app.forms import *
def register(request):
    d={'UF':UserForm()}
    if request.method=='POST':
        UFO=UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return HttpResponse("<h1>registration done successfull</h1>")



    return render(request,'app/register.html',d)


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username,'QO':Question.objects.all()}
        return render(request,'app/home.html',d)
    return render(request,'app/home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['na']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('QuestionList'))
    return render(request,'app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def questionraise(request):
    if request.method=='POST':
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        
        question=request.POST['qu']
        QO=Question.objects.get_or_create(username=UO,question=question)[0]
        QO.save()
        return HttpResponse('<h1>Question posted successfully</h1>')

    return render(request,'app/questions.html')

@login_required
def answering(request):
    return render(request,'app/answerform.html')
    
