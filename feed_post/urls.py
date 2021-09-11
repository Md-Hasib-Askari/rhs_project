from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.feed_post, name='feed_post'),

    # Jobs Page of webpages
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<str:id>', views.job, name='job'),

    # Admission Notice Page of webpages
    path('admission_notice/', views.admission_notices, name='admission_notices'),
    path('admission_notice/<str:id>', views.admission_notice, name='admission_notice'),

]