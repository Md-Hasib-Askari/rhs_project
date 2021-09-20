from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 


# FEED SECTION
class NewsFeed(models.Model):
    privacy = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('draft', 'Draft'),
    ]
    post_title = models.CharField(max_length=256)
    post_content = RichTextUploadingField()
    post_thumbnail = models.ImageField(upload_to='feeds/',blank=True)
    privacy = models.CharField(max_length=50,choices=privacy)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_author = models.CharField(max_length=100, editable=False, blank=True)

    def __str__(self):
        return self.post_title

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Add New Post'


# JOBS SECTION
class JobsBoard(models.Model):
    job_title = models.CharField(max_length=256)
    job_content = RichTextUploadingField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    job_author = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.job_title

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Jobs Board'


# ADMISSION NOTICE SECTION
class AdmissionNotice(models.Model):
    admission_notice_title = models.CharField(max_length=256)
    admission_notice_content = RichTextUploadingField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    admission_notice_author = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.admission_notice_title

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Admission Notice'


# SIDEBAR SECTION - |~|Notice Board|~|
class NoticeBoard(models.Model):
    notice_title = models.CharField(max_length=256)
    notice_content = RichTextUploadingField()
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    notice_author = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.notice_title

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Notice Board'
