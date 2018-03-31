from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required

def catalog(request):
    return render(request, 'catalog.html', {} )

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def map(request):
    return render(request, 'vworld/map.html', {})

def search(request):
    return render(request, 'dbpia/search.html', {})

# ---------------------------------------------------------------
# dbpia 연동하기
# ---------------------------------------------------------------

from webapp.utils import dbpia_collector as dbpia

def response(request):
    keyword = request.GET.get('keyword')
    count = request.GET.get('count')

#    get_file = "/home/hadoop/jsoh/pywebapp/my-first-webapp/webapp/static/temp/result.txt";
    get_file = "c:/Users/JSOH/Desktop/PyCharm Projects/project4future/webapp/static/temp/result.txt";

    get_count = "20";
    get_count = dbpia.dbpia_search_main(keyword, count, "23eb10cd1ceea4cc8c763ad62d34a7c4", get_file)

    context = {
        'in_keyword' : keyword,
        'in_count' : count,
        'get_file' : get_file,
        'get_count' : get_count
    }
    return render_to_response('dbpia/search_response.html', context)

def preview(request):
    return render(request, 'dbpia/txt_preview.html', {})

# ---------------------------------------------------------------
# bootstrap 연동하기
# ---------------------------------------------------------------

def starter_template(request):
    return render(request, 'bootstrap/starter_template/index.html', {})

def cover(request):
    return render(request, 'bootstrap/cover/index.html', {})

def dashboard(request):
    return render(request, 'bootstrap/dashboard/index.html', {})

def blog(request):
    return render(request, 'bootstrap/webapp/index.html', {})

def carousel(request):
    return render(request, 'bootstrap/carousel/index.html', {})

def grid(request):
    return render(request, 'bootstrap/grid/index.html', {})

def jumbotron(request):
    return render(request, 'bootstrap/jumbotron/index.html', {})

def jumbotron_narrow(request):
    return render(request, 'bootstrap/jumbotron_narrow/index.html', {})

def justified_nav(request):
    return render(request, 'bootstrap/justified_nav/index.html', {})

def navbar(request):
    return render(request, 'bootstrap/navbar/index.html', {})

def navbar_fixed_top(request):
    return render(request, 'bootstrap/navbar_fixed_top/index.html', {})

def navbar_static_top(request):
    return render(request, 'bootstrap/navbar_static_top/index.html', {})

def non_responsive(request):
    return render(request, 'bootstrap/non_responsive/index.html', {})

def offcanvas(request):
    return render(request, 'bootstrap/offcanvas/index.html', {})

def signin(request):
    return render(request, 'bootstrap/signin/index.html', {})

def sticky_footer(request):
    return render(request, 'bootstrap/sticky_footer/index.html', {})

def sticky_footer_navbar(request):
    return render(request, 'bootstrap/sticky_footer_navbar/index.html', {})

def theme(request):
    return render(request, 'bootstrap/theme/index.html', {})

def tooltip_viewport(request):
    return render(request, 'bootstrap/tooltip_viewport/index.html', {})

# ---------------------------------------------------------------
# 블루마린
# ---------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

import datetime

""" 임시로 막음
def bluemarlin(request):

    # cookie 테스트(1)
    request.session['my_car'] = 'sonata'
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    response = render(request, 'bluemarline/home.html', {})

    # cookie 테스트(2)
    response.set_cookie('visit_time', datetime.datetime.now())

    return response
"""

def bluemarlin(request):
    return render(request, 'bluemarline/home.html', {})

def under_construct(request):
    return render(request, 'bluemarline/under_construct.html', {})

def about_us(request):

    # 쿠키와 user 객체의 사용방법 테스트 (1)
    print(request.session['my_car']) # cookie 테스트
    print(request.session['num_visits'])

    if request.user.is_authenticated:
        print(request.user.username)
    else:
        print("로그인 후 이용해 주세요")

    # 쿠키와 user 객체의 사용방법 테스트 (1)
    print(request.COOKIES['visit_time'])

    return render(request, 'bluemarline/about_us.html', {})

@login_required
def bl_dashboard(request):
    return render(request, 'bluemarline/dashboard.html', {})

@login_required
def sna_blog(request):
    return render(request, 'bluemarline/sna_blog.html', {})

# ---------------------------------------------------------------
# 로그인
# ---------------------------------------------------------------

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

# ---------------------------------------------------------------
# 다이얼로그 플로우
# ---------------------------------------------------------------

def welcome_dialogflow(request):
    return render(request, 'welcome_dialogflow.html', {})