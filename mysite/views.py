from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名：<input type='text' name='username'>
    <input type='submit' value='提交'>
<form>
'''

def frontpage_view(request):
    return HttpResponse("首页")

def page1_view(request):
    return HttpResponse("Hello World")

def page2_view(request):
    return HttpResponse("第2页")

def page_view(request, pageNumber):
    s = "This is the page of number {}".format(pageNumber)
    return HttpResponse(s)

def calculate(operator1, sign, operator2):
    if (sign == "add"):
        result = operator1 + operator2
    elif (sign == "sub"):
        result = operator1 - operator2
    elif (sign == "mul"):
        result = operator1 * operator2
    elif (sign == "div"):
        result = operator1 / operator2 if operator2 != 0 else "404 Not Found"
    else:
        result = "404 Not Found"
    return result

def cal(request, operator1, sign, operator2):
    result = calculate(operator1, sign, operator2)
    return HttpResponse(result)


def cal2(request: HttpRequest):
    ls1 = request.GET.getlist('a')
    ls2 = request.GET.getlist('b')
    ls_sign = request.GET.getlist('sign')

    result = "404 Not Found"
    if len(ls1) != 1 or len(ls2) != 1 or len(ls_sign) != 1:
        result = "404 Not Found"
    else:
        result = calculate(eval(ls1[0]), ls_sign[0], eval(ls2[0]))
        result = "The result is {}".format(result)

    return HttpResponse(result)


def request_test(request: HttpRequest):
    print("the path info is {}".format(request.path_info))
    print("the full path is ", request.get_full_path())
    print("the method is " + request.method)
    print("the query is {}".format(request.GET))
    # return HttpResponse("request test")
    return HttpResponseRedirect('page1')

def test_get_post(request: HttpRequest):
    if request.method == "GET":
        print("a : ", request.GET.get('a'))
        print("a : ", request.GET.getlist('a'))
        return HttpResponse(POST_FORM)
    elif request.method == "POST":
        print("username is ", request.POST.get('username', 'None'))
        return HttpResponse("post is OK")
    else:
        pass

    return HttpResponse("test get and post")

def test_html(request: HttpRequest):
    #方案1
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)

    #方案2
    dic = {'username': '123', 'age': 18}
    return render(request, 'test_html.html', dic)

def test_html_param(request: HttpRequest):
    dic = {}
    dic['int'] = 88
    dic['str'] = 'name'
    dic['list'] = ['Tom', 'Jack', 'Lily']
    dic['dict'] = {'a': 9, 'b': 8}
    dic['func'] = say_hi
    dic['class_obj'] = Dog()
    dic['script'] = '<script>alert(1111)</script>'

    return render(request, 'test_html_param.html', dic)

def say_hi():
    return "hahaha"

class Dog:
    def say(self):
        return 'wangwang'


def test_if_for(request: HttpResponse):
    dic = {}
    dic['x'] = 10
    dic['list'] = ['Tom', 'Jack', 'Lily']
    return render(request, 'test_if_for.html', dic)


def test_mycal(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        #处理计算
        x = eval(request.POST.get('x', 0))
        y = eval(request.POST.get('y', 0))
        op = request.POST.get('op', 'add')

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y if y != 0 else 'Wrong'
        else:
            pass

        return render(request, 'mycal.html', locals())
    else:
        pass

def base_view(request: HttpRequest):
    lst = ['Tom', 'Jack']
    return render(request, 'base.html', locals())

def music_view(request: HttpRequest):
    return render(request, 'music.html')

def sport_view(request: HttpRequest):
    return render(request, 'sport.html')

def test_url(request: HttpRequest):
    return render(request, 'test_url.html')

def test_url_result(request: HttpRequest, age):
    from django.urls import reverse
    url = reverse('base_index')
    return HttpResponseRedirect(url)
    # return HttpResponse("---test url res is ok")



