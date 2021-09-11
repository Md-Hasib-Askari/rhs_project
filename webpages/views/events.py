from django.shortcuts import render

from webpages.common_db_imports import *
from webpages.models import StaticPage

# Create your views here.
def celebrations(request):
    page_content = StaticPage.objects.get(slug='celebrations')
    context['page_content'] = page_content

    template_name = 'webpages/events/celebrations.html'

    return render(request, template_name, context)

def sports(request):
    page_content = StaticPage.objects.get(slug='sports')
    context['page_content'] = page_content

    template_name = 'webpages/events/sports.html'

    return render(request, template_name, context)

def cultural_activities(request):
    page_content = StaticPage.objects.get(slug='cultural_activities')
    context['page_content'] = page_content

    template_name = 'webpages/events/cultural_activities.html'

    return render(request, template_name, context)

def publications(request):
    page_content = StaticPage.objects.get(slug='publications')
    context['page_content'] = page_content

    template_name = 'webpages/events/publications.html'

    return render(request, template_name, context)


