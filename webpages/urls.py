from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import academics, administration, admission, at_a_glance, events, gallery, contact_us
from core.views import home

urlpatterns = [
    path('', home, name='home'),

    # Navigation - At a Glance 
    path('welcome_note/', at_a_glance.welcome_note, name='welcome_note'),
    path('about_us/', at_a_glance.about_us, name='about_us'),
    path('vision_mission/', at_a_glance.vision_mission, name='vision_mission'),
    path('principal_message/', at_a_glance.principal_message, name='principal_message'),
    path('governing_body/', at_a_glance.governing_body, name='governing_body'),
    path('curriculum/', at_a_glance.curriculum, name='curriculum'),
    path('maps/', at_a_glance.maps, name='maps'),

    # Navigation - Administration 
    path('calendar/', administration.calendar, name='calendar'),
    path('time/', administration.time, name='time'),
    path('notices/', administration.notices, name='notices'),
    path('notice/<str:id>', administration.notice, name='notice'),

    path('teachers_info/', administration.teachers_info, name='teachers_info'),
    path('staffs_info/', administration.staffs_info, name='staffs_info'),
    path('student_statistics/', administration.student_statistics, name='student_statistics'),

    # Navigation - Academics 
    path('rules_regulations/', academics.rules_regulations, name='rules_regulations'),
    path('teaching_method/', academics.teaching_method, name='teaching_method'),
    path('teachers_training/', academics.teachers_training, name='teachers_training'),
    path('student_support/', academics.student_support, name='student_support'),
    path('scholarship/', academics.scholarship, name='scholarship'),
    path('result/', academics.result, name='result'),
    path('co_curricular_activities/', academics.co_curricular_activities, name='co_curricular_activities'),
    path('facilities/', academics.facilities, name='facilities'),
    path('faculties_staffs/', academics.faculties_staffs, name='faculties_staffs'),
    path('prospectus_syllabus/', academics.prospectus_syllabus, name='prospectus_syllabus'),

    # Navigation - Admission 
    path('jsc/', admission.jsc, name='jsc'),
    path('ssc/', admission.ssc, name='ssc'),
    path('fee_payment_procedure/', admission.fee_payment_procedure, name='fee_payment_procedure'),

    # Navigation - Events 
    path('celebrations/', events.celebrations, name='celebrations'),
    path('sports/', events.sports, name='sports'),
    path('cultural_activities/', events.cultural_activities, name='cultural_activities'),

    # Navigation - Gallery 
    path('photo_gallery/', gallery.photo_gallery, name='photo_gallery'),
    path('video_gallery/', gallery.video_gallery, name='video_gallery'),

     # Navigation - Contact Us 
    path('contact_us/', contact_us.contact_us, name='contact_us'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)