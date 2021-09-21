from django.shortcuts import render

from webpages.common_db_imports import extractData
from webpages.models import StaticPage


# Create your views here.
def jsc(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='jsc')
    context['page_content'] = page_content

    template_name = 'webpages/admission/jsc.html'

    return render(request, template_name, context)

def ssc(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='ssc')
    context['page_content'] = page_content

    template_name = 'webpages/admission/ssc.html'

    return render(request, template_name, context)


def fee_payment_procedure(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='fee_payment_procedure')
    context['page_content'] = page_content

    template_name = 'webpages/admission/fee_payment_procedure.html'

    return render(request, template_name, context)
