from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('student_signup', views.student_signup,  name='student_signup'),
    path('teacher_signup', views.teacher_signup,  name='teacher_signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('student_dashboard', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_proctorform/', views.student_proctorform, name='student_proctorform'),
    path('student_updateform/', views.student_updateform, name='student_updateform'),
    path('teacher_viewproctor/', views.teacher_viewproctor, name='teacher_viewproctor'),
    path('index/', views.index, name='index'),
]