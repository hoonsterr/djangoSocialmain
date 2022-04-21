from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TbUser
from django.contrib.auth.hashers import make_password, check_password
from . import models
from .models import Document


def join(request):
    if request.method == "GET":
        return render(request, 'join.html')

    elif request.method == "POST":
        user_nick = request.POST.get['user_nick', None]
        user_email = request.POST.get['user_email', None]
        user_pw = request.POST.get['user_pw', None]
        re_password = request.POST.get['re_password', None]
        res_data = {}

        if not (user_nick and user_pw and user_email and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if user_pw != re_password:
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = TbUser(user_nick=user_nick, user_pw=make_password(user_pw), user_email=user_email)
            user.save()
        return render(request, 'join.html', res_data)


def login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_email = request.POST.get('user_email', None)
        user_pw = request.POST.get('user_pw', None)

        if not (user_email and user_pw):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
        else:
            user = TbUser.objects.get(user_email=user_email)
            # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(user_pw, user.user_pw):
                request.session['user'] = user.user_nick
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html', response_data)


def home(request):
    user_nick = request.session.get('user')
    if user_nick:
        tbuser_info = TbUser.objects.get(pk=user_email)  # pk : primary key
        return HttpResponse(tbuser_info.user_nick)  # 로그인을 했다면, username 출력

    return HttpResponse('로그인 실패')  # session에 user가 없다면, (로그인을 안했다면)


def logout(request):
    request.session['user'] = {}
    request.session.modified = True
    return redirect('/')


def dbconn(request):
    result = TbUser.objects.all()
    data = {
        'result': result,
    }
    return render(request, 'dbconn.html', data)

def homepage(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request, 'mypage.html')

def socialout(request):
    return redirect('/')

def create(request):
    return render(request, 'create.html')

def about(request):
    return render(request, 'about.html')

def trial(request):
    return render(request, 'trial.html')

def result(request):
    return render(request, 'result.html')

def upload(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST.get("fileTitle", None)

        uploadedFile = request.FILES.get("uploadedFile", None)

        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "create.html", context={
        "files": documents
    })
