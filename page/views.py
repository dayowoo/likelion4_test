from django.shortcuts import render, redirect
from .models import Blog
import random
from django.utils import timezone


# Create your views here.
def home(request):
    blogs = Blog.objects.all
    # 모델에게 글을 받아서 "blogs"라는 이름으로 템플릿에 전달
    return render(request, 'home.html', {"blogs":blogs})

def new(request):
    return render(request, "new.html")

# 전달받은 데이터를 저장하는 함수
def create(request):
    #request 안에 title, content 라는 이름의 데이터를 가져와서 변수에 담아놓음
    title = request.GET["title"]
    content = request.GET["content"]
    # Blog 빈 틀을 하나 만들고 그 안에 사용자에게 받은 데이터 넣고 현재 시간 넣고 저장
    blog = Blog()
    blog.title = title
    blog.content = content
    blog.time = timezone.now()
    blog.save()
    # redirect : 다른 url로 연결해주는 기능
    return redirect("home")



# Lotto 예제
# 이 함수가 실행될 경우 lotto.html을 보여줘라
def lotto(request):
    # 랜덤하게 생성된 수를 잠시 넣을곳(변수) = 1이상 46미만의 수 하나 생성
    첫번째 = random.randrange(1,46)
    두번째 = random.randrange(1,46)
    세번째 = random.randrange(1,46)
    네번째 = random.randrange(1,46)
    다섯번째 = random.randrange(1,46)
    여섯번째 = random.randrange(1,46)
    보너스 = random.randrange(1,46)
    # {"이름":값(변수)} : "첫번째"라는 변수를 a라는 이름으로 lotto.html에 넘겨줘라
    return render(request, "lotto.html", {
        "a": 첫번째,
        "b": 두번째,
        "c": 세번째,
        "d": 네번째,
        "e": 다섯번째,
        "f": 여섯번째,
        "bonus": 보너스
        })
