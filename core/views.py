from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.shortcuts import render, redirect

from webpages.common_db_imports import *

from dashboard.models import HeaderInfo, HomeSlider, SideBarBanner, UsefulLink
from feed_post.models import NewsFeed, NoticeBoard
from .models import IPAddress

# Create your views here.
def home(request):
    # IP Check
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    IPAddress.objects.create(ip_address = ip)

    # Slider Section
    slider_images = HomeSlider.objects.all()[::-1]
    slider_images = slider_images[:5]

    # Feed Posts Section
    feed_posts = NewsFeed.objects.all()[::-1]
    # Pagination for Feed Post
    paginator = Paginator(feed_posts, 8)
    page_number = request.GET.get('page')
    feedpost_page_obj = paginator.get_page(page_number)

    context_list = [('slider_images', slider_images), ('page_obj', feedpost_page_obj)]
    for key, value in context_list:
        context[key] = value
    
    return render(request, 'core/home.html', context)



