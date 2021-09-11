from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Posts for static pages
class StaticPage(models.Model):
    MAIN_NAV = (
        ('at_a_glance', 'At a Glance'),
        ('academics', 'Academics'),
        ('administration', 'Administration'),
        ('admission', 'Admission '),
        ('events', 'Events '),
        ('gallery', 'Gallery'),
        ('contact_us', 'None'),
    )

    page_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, primary_key=True)
    category = models.CharField(max_length=14, choices=MAIN_NAV, default='None')
    page_content = RichTextUploadingField(blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.page_name
    
    class Meta:
        verbose_name_plural = 'Static Pages Data'