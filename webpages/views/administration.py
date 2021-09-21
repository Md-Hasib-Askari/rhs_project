from django.shortcuts import render

from webpages.common_db_imports import extractData
from webpages.models import StaticPage

# Create your views here.
def calendar(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='calendar')
    context['page_content'] = page_content

    template_name = 'webpages/administration/calendar.html'

    return render(request, template_name, context)

def time(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='time')
    context['page_content'] = page_content

    template_name = 'webpages/administration/time.html'

    return render(request, template_name, context)

def jobs(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='jobs')
    context['page_content'] = page_content

    template_name = 'webpages/administration/jobs.html'

    return render(request, template_name, context)


def teachers_info(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='teachers_info')
    context['page_content'] = page_content

    template_name = 'webpages/administration/teachers_info.html'

    return render(request, template_name, context)


def staffs_info(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='staffs_info')
    context['page_content'] = page_content

    template_name = 'webpages/administration/staffs_info.html'

    return render(request, template_name, context)

def student_statistics(request):
    context = extractData()

    page_content = StaticPage.objects.get(slug='student_statistics')
    context['page_content'] = page_content

    template_name = 'webpages/administration/student_statistics.html'

    return render(request, template_name, context)




