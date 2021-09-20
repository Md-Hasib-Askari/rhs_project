from django.shortcuts import render
from django.core.paginator import Paginator

from webpages.common_db_imports import *
from .models import NewsFeed, JobsBoard, AdmissionNotice

# Home Page Feed Posts
def feed_post(request, id):
    feed_post = NewsFeed.objects.get(id=id)
    context['feed_post'] = feed_post
    return render(request, 'feed_post/feed_post.html', context)


# All Jobs
def jobs(request):
    jobs = JobsBoard.objects.all()[::-1]

    # Pagination from Job Post
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    jobs_post_page_obj = paginator.get_page(page_number)
    context_list = [('page_obj', jobs_post_page_obj)]
    for key, value in context_list:
        context[key] = value
    
    return render(request, 'feed_post/jobs.html', context)


# Single Job
def job(request, id):
    job = JobsBoard.objects.get(id=id)

    context_list = [('single_job', job)]
    for key, value in context_list:
        context[key] = value
    
    return render(request, 'feed_post/job.html', context)


# All Admission Notices
def admission_notices(request):
    admission_notices = AdmissionNotice.objects.all()[::-1]

    # Pagination from Job Post
    paginator = Paginator(admission_notices, 5)
    page_number = request.GET.get('page')
    admission_notice_page_obj = paginator.get_page(page_number)
    context_list = [('page_obj', admission_notice_page_obj)]
    for key, value in context_list:
        context[key] = value
    
    return render(request, 'feed_post/admission_notices.html', context)


# Single Admission Notice
def admission_notice(request, id):
    admission_notice = AdmissionNotice.objects.get(id=id)

    context_list = [('single_admission_notice', admission_notice)]
    for key, value in context_list:
        context[key] = value
    
    return render(request, 'feed_post/admission_notice.html', context)

# All Admission Notices
def notices(request):
    template_name = 'feed_post/notices.html'

    return render(request, template_name, context)

# Single Admission Notice
def notice(request, id):
    single_notice = NoticeBoard.objects.get(id=id)

    context['single_notice'] = single_notice
    template_name = 'feed_post/notice.html'
    return render(request, template_name, context)
