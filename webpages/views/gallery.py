from django.shortcuts import render

from webpages.common_db_imports import *
from webpages.models import StaticPage


# Create your views here.
def photo_gallery(request):
    page_content = StaticPage.objects.get(slug='photo_gallery')
    context['page_content'] = page_content

    template_name = 'webpages/gallery/photo_gallery.html'

    return render(request, template_name, context)

def video_gallery(request):
    page_content = StaticPage.objects.get(slug='video_gallery')
    context['page_content'] = page_content

    template_name = 'webpages/gallery/video_gallery.html'

    return render(request, template_name, context)
