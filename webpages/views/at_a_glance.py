from django.shortcuts import render

from webpages.common_db_imports import extractData
from webpages.models import StaticPage

# Create your views here.
def welcome_note(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='welcome_note')
    context['page_content'] = page_content

    template_name = 'webpages/at_a_glance/welcome_note.html'
    return render(request, template_name, context)

def about_us(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='about_us')
    context['page_content'] = page_content


    template_name = 'webpages/at_a_glance/about_us.html'
    return render(request, template_name, context)

def vision_mission(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='vision_mission')
    context['page_content'] = page_content

    template_name = 'webpages/at_a_glance/vision_mission.html'
    return render(request, template_name, context)

def principal_message(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='principal_message')
    context['page_content'] = page_content

    template_name = 'webpages/at_a_glance/principal_message.html'
    return render(request, template_name, context)

def governing_body(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='governing_body')
    context['page_content'] = page_content

    template_name = 'webpages/at_a_glance/governing_body.html'
    return render(request, template_name, context)

def curriculum(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='curriculum')
    context['page_content'] = page_content
    
    template_name = 'webpages/at_a_glance/curriculum.html'
    return render(request, template_name, context)

def maps(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='maps')
    context['page_content'] = page_content

    template_name = 'webpages/at_a_glance/maps.html'
    return render(request, template_name, context)

