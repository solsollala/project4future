from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required


# ---------------------------------------------------------------
# 블루마린
# ---------------------------------------------------------------

from django.http import HttpResponseRedirect
from django.contrib.auth import logout

import datetime

def bluemarlin(request):
    return render(request, 'bluemarline/home.html', {})

# ---------------------------------------------------------------
# 로그인
# ---------------------------------------------------------------

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

