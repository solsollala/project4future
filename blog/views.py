from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .models import Post

def hello(request):
    return render(request, 'hello.html', {} )

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

from blog.utils import dbpia_collector as dbpia

def response(request):
    keyword = request.GET.get('keyword')
    count = request.GET.get('count')

#    get_file = "/home/hadoop/jsoh/pywebapp/my-first-blog/blog/static/temp/result.txt";
    get_file = "c:/Users/JSOH/Desktop/PyCharm Projects/djangogirls/blog/static/temp/result.txt";

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
    return render(request, 'bluemarine/starter_template/index.html', {})

def cover(request):
    return render(request, 'bluemarine/cover/index.html', {})

def dashboard(request):
    return render(request, 'bluemarine/dashboard/index.html', {})

def blog(request):
    return render(request, 'bluemarine/blog/index.html', {})

def carousel(request):
    return render(request, 'bluemarine/carousel/index.html', {})

def grid(request):
    return render(request, 'bluemarine/grid/index.html', {})

def jumbotron(request):
    return render(request, 'bluemarine/jumbotron/index.html', {})

def jumbotron_narrow(request):
    return render(request, 'bluemarine/jumbotron_narrow/index.html', {})

def justified_nav(request):
    return render(request, 'bluemarine/justified_nav/index.html', {})

def navbar(request):
    return render(request, 'bluemarine/navbar/index.html', {})

def navbar_fixed_top(request):
    return render(request, 'bluemarine/navbar_fixed_top/index.html', {})

def navbar_static_top(request):
    return render(request, 'bluemarine/navbar_static_top/index.html', {})

def non_responsive(request):
    return render(request, 'bluemarine/non_responsive/index.html', {})

def offcanvas(request):
    return render(request, 'bluemarine/offcanvas/index.html', {})

def signin(request):
    return render(request, 'bluemarine/signin/index.html', {})

def sticky_footer(request):
    return render(request, 'bluemarine/sticky_footer/index.html', {})

def sticky_footer_navbar(request):
    return render(request, 'bluemarine/sticky_footer_navbar/index.html', {})

def theme(request):
    return render(request, 'bluemarine/theme/index.html', {})

def tooltip_viewport(request):
    return render(request, 'bluemarine/tooltip_viewport/index.html', {})