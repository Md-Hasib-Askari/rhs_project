from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 

# HEADER SECTION
class HeaderInfo(models.Model):
    favicon = models.ImageField(upload_to='images/favicon', blank=True, null=True)
    phone_no = models.CharField(max_length=17)
    email = models.EmailField(blank=True)
    logo = models.ImageField(upload_to='images/logo/', blank=True,null=True)
    header_title = models.CharField(max_length=256)
    header_slogan = models.CharField(max_length=256)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, editable=False)


    def __str__(self):
        return 'Header Information'

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Header Information'

# SLIDER SECTION
class HomeSlider(models.Model):
    slider_image = models.ImageField(upload_to='images/slider')
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slider_author = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return str(self.slider_author)

    # Admin Panel Title
    class Meta:
        verbose_name_plural = 'Add Slider Image'


# SIDEBAR SECTION - |~|Banner Image|~|
class SideBarBanner(models.Model):
    banner_image = models.ImageField(upload_to='images/sidebar_banner')
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, editable=False)

    

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name_plural = 'Add Banner Image'


# SIDEBAR SECTION - |~|Useful Links|~|
class UsefulLink(models.Model):
    link_title = models.CharField(max_length=256, null=True)
    link_url = models.CharField(max_length=256)
    posted_on  = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    link_author = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.link_title
