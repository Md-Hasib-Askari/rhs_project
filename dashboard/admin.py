from django.contrib import admin

from dashboard.models import HeaderInfo, HomeSlider, SideBarBanner,  UsefulLink

# HEADER SECTION
@admin.register(HeaderInfo)
class HeaderInfoAdmin(admin.ModelAdmin):
    list_display = ['phone_no', 'email', 'logo', 'header_title', 'header_slogan', 'updated_on', 'author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.author:
            instance.author = request.user
        instance.save()
        return instance            

# SLIDER SECTION
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['slider_image', 'updated_on', 'slider_author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.slider_author:
            instance.slider_author = request.user
        instance.save()
        return instance


# SIDEBAR SECTION - |~|Banner Image|~|
@admin.register(SideBarBanner)
class SideBarBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'banner_image', 'updated_on', 'author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.author:
            instance.author = request.user
        instance.save()
        return instance


# SIDEBAR SECTION - |~|Useful Links|~|
@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ['link_title', 'link_url', 'updated_on', 'link_author',]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.link_author:
            instance.link_author = request.user
        instance.save()
        return instance
