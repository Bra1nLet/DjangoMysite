from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.
def index(response):
    return render(response, 'polls/startpage.html')


def register(request):
    if request.method == "POST":
        login = request.POST["user"]
        password = request.POST["pass"]
        nickname = request.POST["nick"]
        dict1 = {
            'nickname': nickname,
            'login': login,
            'password': password
        }
        a = models.Userr(Login=login, Password=password, Nickname=nickname)
        a.save()
        return Mycabinet(request, dict1)
    return render(request, 'polls/Register.html')


def Mycabinet(request, dictt):
    return render(request, 'polls/Mycabinet.html', dictt)

def auth(request):
    print(models.Userr)
    if request.method == "POST":
        login = request.POST["user"]
        password = request.POST["pass"]
        dict1 = {
            'login': login,
            'password': password
        }
        #return Mycabinet(request, dict1)
    return render(request, 'polls/Login.html')
