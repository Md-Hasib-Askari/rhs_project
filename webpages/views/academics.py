from django.shortcuts import render

from webpages.common_db_imports import *
from webpages.models import StaticPage


# Create your views here.
def rules_regulations(request):
    page_content = StaticPage.objects.get(slug='rules_regulations')
    context['page_content'] = page_content

    template_name = 'webpages/academics/rules_regulations.html'
    return render(request, template_name, context)


def teaching_method(request):
    page_content = StaticPage.objects.get(slug='teaching_method')
    context['page_content'] = page_content

    template_name = 'webpages/academics/teaching_method.html'
    return render(request, template_name, context)


def teachers_training(request):
    page_content = StaticPage.objects.get(slug='teachers_training')
    context['page_content'] = page_content

    template_name = 'webpages/academics/teachers_training.html'
    return render(request, template_name, context)


def student_support(request):
    page_content = StaticPage.objects.get(slug='student_support')
    context['page_content'] = page_content

    template_name = 'webpages/academics/student_support.html'
    return render(request, template_name, context)


def scholarship(request):
    page_content = StaticPage.objects.get(slug='scholarship')
    context['page_content'] = page_content

    template_name = 'webpages/academics/scholarship.html'
    return render(request, template_name, context)


def result(request):
    page_content = StaticPage.objects.get(slug='result')
    context['page_content'] = page_content

    template_name = 'webpages/academics/result.html'
    return render(request, template_name, context)

    
def co_curricular_activities(request):
    page_content = StaticPage.objects.get(slug='co_curricular_activities')
    context['page_content'] = page_content


    template_name = 'webpages/academics/co_curricular_activities.html'
    return render(request, template_name, context)


def facilities(request):
    page_content = StaticPage.objects.get(slug='facilities')
    context['page_content'] = page_content

    template_name = 'webpages/academics/facilities.html'
    return render(request, template_name, context)


def faculties_staffs(request):
    page_content = StaticPage.objects.get(slug='faculties_staffs')
    context['page_content'] = page_content

    template_name = 'webpages/academics/faculties_staffs.html'
    return render(request, template_name, context)


def prospectus_syllabus(request):
    page_content = StaticPage.objects.get(slug='prospectus_syllabus')
    context['page_content'] = page_content

    template_name = 'webpages/academics/prospectus_syllabus.html'
    return render(request, template_name, context)




