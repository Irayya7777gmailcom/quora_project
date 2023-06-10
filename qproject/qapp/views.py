from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import postqu,signup
from django.db.models import Count

def main(request):
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        l=request.POST['l']
        p=request.POST['p']
        c1=signup.objects.all()
        for i in c1:
            if l==i.user:
                if p==i.passwd:
                    return redirect('/post')
        return render(request,'login.html',{'r':'INVALID DETAILS'})
    return render(request,'login.html')

def sign(request):
    if request.method=='POST':
        l=request.POST['l']
        p=request.POST['p']
        c1=signup.objects.create(user=l,passwd=p)
        c1.save()
        return redirect('/login')
    return render(request,'signup.html')
        



def post(request):
    return render(request,'post.html')

def post_question(request):
    if request.method=='POST':
        q=request.POST['q']
        c1=postqu.objects.create(question=q)
        c1.save()
        
        return render(request,'post.html',{'d':'posted'})
    
def posted(request):
    c1=postqu.objects.all()
    
    return render(request,'posted.html',{'d':c1})
    
def answer(request):
    if request.method=='POST':
        a=request.POST['id']
        ans=request.POST['ans']
        c2=postqu.objects.get(id=a)
        if c2:
            c2.answers=ans
            c2.save()
            return HttpResponse('success')
        else:
            return HttpResponse('not success')
    return HttpResponse('enter valid url path')
        
def posted_ans(request):
        
        c1=postqu.objects.all()
        return render (request,'posted_ans.html',{'data':c1})
        
def like(request):
    if request.method=='POST':
        li=request.POST['lik']
        c1=postqu.objects.get(id=li)
        c1.like='yes'
        c1.save()
        c2=postqu.objects.all()
        c = c2.filter(like='yes').count()
        return redirect('/posted_ans')

        
