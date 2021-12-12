from django.http import HttpResponse,HttpResponseRedirect
from django.http import request

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















