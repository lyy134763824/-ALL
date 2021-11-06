from django.http import HttpResponse,HttpResponseRedirect
from django.http import request

def pagen_view(request,n):

    html = f"<h1>dddd-{n}</h1>"
    return HttpResponse(html)

def page_calculate(request,n1,symbol,n2):
    if n1.isdigit() and n2.isdigit():
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