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

    # 일단 여기서 크롤링 해 보자
    get_file = "c:/temp/temp.txt";
    get_count = "20";
    get_count = dbpia.dbpia_search_main(keyword, count, "23eb10cd1ceea4cc8c763ad62d34a7c4", get_file)

    context = {
        'in_keyword' : keyword,
        'in_count' : count,
        'get_file' : get_file,
        'get_count' : get_count
    }
    return render_to_response('dbpia/search_response.html', context)
