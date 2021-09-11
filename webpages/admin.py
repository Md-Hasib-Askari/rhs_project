from django.contrib import admin

from .models import StaticPage

# Posts for static pages
@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = [ 'slug', 'page_name', 'category', 'updated_on', 'author', ]

    def save_model(self, request, instance, form, change):
        form = form.save(commit=False)
        if not change or not instance.author:
            instance.author = request.user
        instance.save()
        return instance