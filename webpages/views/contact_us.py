from django.shortcuts import render

from webpages.common_db_imports import extractData
from webpages.models import StaticPage


# Create your views here.
def contact_us(request):
    context = extractData()
    
    page_content = StaticPage.objects.get(slug='contact_us')
    context['page_content'] = page_content

    template_name = 'webpages/contact_us.html'
    return render(request, template_name, context)

