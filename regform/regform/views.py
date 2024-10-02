from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import datas
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def first(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logreg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin@gmail.com' and password == 'admin':
            request.session['logint'] = 'email'
            request.session['logint'] = 'password'
            return render(request, 'index.html')
        elif datas.objects.filter(email=email, password=password).exists():
            user = datas.objects.get(email=email, password=password)
            request.session['uid'] = user.id  
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

def regs(request):
    return render(request, 'reg.html')

def regform(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('email')
        d = request.POST.get('password')
        x = datas(name=a, phone=b, email=c, password=d)
        x.save()
    return render(request, 'index.html')

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def viewuser(request):
    a=datas.objects.all()
    return render(request,'select.html',{'result':a})

def profile(request):
    sel=datas.object.get(id=request.session[uid])
    return render(request,'new.html',{'result':sel})

def deleteuser(request,id):
    sel=datas.objects.get(id=id)
    sel.delete()
    return redirect(viewuser)


def updateuser(request,id):

    sel=datas.objects.get(id=id)
   
    return render(request,'update.html',{'result':sel})

def addupdate(request,id):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('email')
        d = request.POST.get('password')
        x = datas(name=a, phone=b, email=c, password=d,id=id)
        x.save()
    return redirect(viewuser)
