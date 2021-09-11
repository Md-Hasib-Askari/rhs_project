from django.contrib import admin

from .models import NewsFeed, JobsBoard, NoticeBoard, AdmissionNotice

# FEED SECTION
@admin.register(NewsFeed)
class NewsFeedAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_content', 'post_thumbnail', 'privacy', 'updated_on', 'post_author',]
    
    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.post_author:
            instance.post_author = request.user
        instance.save()
        return instance 


# JOBS SECTION
@admin.register(JobsBoard)
class JobsBoardAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_content', 'updated_on', 'job_author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.job_author:
            instance.job_author = request.user
        instance.save()
        return instance

# ADMISSION NOTICE SECTION
@admin.register(AdmissionNotice)
class AdmissionNotice(admin.ModelAdmin):
    list_display = ['admission_notice_title', 'admission_notice_content', 'updated_on', 'admission_notice_author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.admission_notice_author:
            instance.admission_notice_author = request.user
        instance.save()
        return instance


# SIDEBAR SECTION - |~|Notice Board|~|
@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ['notice_title', 'notice_content', 'updated_on', 'notice_author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.notice_author:
            instance.notice_author = request.user
        instance.save()
        return instance