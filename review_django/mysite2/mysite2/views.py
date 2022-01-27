from django.http import HttpResponse,HttpResponseRedirect
from django.http import request
from django.shortcuts import render
from django.urls import reverse

def a():
    return ('a hhh')

class A(object):
    def __init__(self):
        pass
    def say(self):
        return ('A 我会说')

def pagen_view(request,page):

    html = f"<h1>dddd-{page}</h1>"
    return HttpResponse(html)

def page_calculate(request,n1,symbol,n2):
    if str(n1).isdigit() and str(n2).isdigit():
        if symbol == 'add':
            res = float(n1)+float(n2)
            html = f"<h1>{n1}+{n2} = {res}</h1>"
            print(request.META['REMOTE_ADDR'])

        elif  symbol == 'sub':
            res = float(n1)-float(n2)
            html = f"<h1>{n1}-{n2} = {res}</h1>"

        elif  symbol == 'mul':
            res = float(n1) * float(n2)
            html = f"<h1>{n1}*{n2} = {res}</h1>"

        else:
            html = f"<h1>输入运算符号错误</h1>"

    else:
        html = f"<h1>输入的不是纯数字</h1>"
        return HttpResponseRedirect('https://www.baidu.com/')
    return HttpResponse(html)

def index_view(request):
    html='''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL / was not found on this server.</p>
</body></html>
    '''

    return HttpResponse(html)


def test_view(request):
    print('path',request.path_info)
    print('method',request.method)
    print('get',request.GET)
    print('body',request.body)
    print('full_path',request.get_full_path())
    print('meta',request.META)
    # return HttpResponse('ok')
    return HttpResponseRedirect('/page/5')

def test_post(request):
    if request.method == 'GET':
        value = request.GET.get('C',None)
        if not value:
            return HttpResponse('Value not get')
        
        print(value)
        return HttpResponse('ok')
    elif request.method =='POST':
        pass
    else:
        return HttpResponse('暂时不支持此功能')


def test_render(request):
    divt = {"username":"lyy","age":"18"}
    return render(request,'login2.html',divt)

def test_render2(request):
    divt = {"username":"lyy","age":"18"}
    divt['dict'] = {'d':1}
    divt['l']= [1,2,3]
    divt['func'] = a
    divt['class_obj'] = A()
    divt['script'] = "<script >alert(1111)</script>"
    return render(request,'params.html',divt)

def mycal(request):
    if request.method =='GET':
        return render(request,'bq.html')
    elif request.method =='POST':
        x = float(request.POST.get('x'))
        y = float(request.POST.get('y'))
        op = request.POST.get('op')
        if op =='add':
            res = x+y
        elif op =='mul':
            res = x*y
        elif op =='div':
            res = x/y
        else:
            res = x - y
        return render(request,'bq.html',locals())


def base_view(request):
    return render(request,'base.html')

def music_view(request):
    return render(request,'music.html')

def sport_view(request):
    return render(request,'sport.html')

def reverse_view(request):
    url = reverse('person',args=[10,20])
    # url = reverse('person',kwargs={'name':'kk','age':20,})
    print(url)
    return HttpResponseRedirect(url)


def person_view(request,age=None,name=None):
    if request.method == 'GET':
        return render(request,'person.html',locals())


def static_view(request):

    return render(request,'static.html')

