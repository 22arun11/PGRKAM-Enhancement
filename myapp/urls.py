from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('404.html',views.fun404,name='fun404'),
    path('about.html',views.about,name='about'),
    path('category.html',views.category,name='category'),
    path('contact.html',views.contact,name='contact'),
    path('job-list.html',views.joblist,name='joblist'),
    path('testimonial.html',views.testimonial,name='testimonial'),
    path('job-detail.html',views.jobdetail,name='jobdsetail'),
    path('resume.html',views.resume,name='resume'),
    path('chat.html',views.chat,name='chat'),]


