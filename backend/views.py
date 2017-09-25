from django.shortcuts import render
from django.http import HttpResponse
from backend.models import User
from django.views.decorators.csrf import csrf_exempt
from backend.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
USER_LIST = []
for i in range(1, 666):
    temp = {'name':'root'+str(i), 'age':i}
    USER_LIST.append(temp)



#注册
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        print("regist")
        username = request.POST['username']
        password = request.POST['password']
        k = User.objects.create(username=username,password=password)
        k.save()
        return HttpResponse('regist success!!!')
    else:
        return render(request,'regist.html')
    if request.method == 'GET' :
        return render(request,'regist.html')
#登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username__exact=username,password__exact=password)
        if user:
            return render(request,"index.html")
        else:
            return HttpResponse('用户密码错误，请再次登录')
    else:
        return render(request,"login.html")

 #首页
def index(request):
    # list = Article.objects.all().order_by('-pk')

    return render(request,"index.html",{"list":list})
