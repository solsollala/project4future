from django.contrib import admin
from .models import Post, Customer, bm_fish_point

admin.site.register(Post)
admin.site.register(Customer)

admin.site.register(bm_fish_point)