from django.urls import path
from Fitness import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login',views.LOGIN,name='login'),
    path('',views.SIGNUP,name='signup'),
    path('logout',views.LOGOUT,name='logout'),

    path('home', views.Home,name='index'),
    path('aboutus',views.Aboutus,name='about_us'),
    path('blog-details',views.BlogDetails ,name='blog_details'),
    path('classes',views.Classes ,name='class'),
    path('Services',views.Services,name='services'),
    path('Team',views.Team,name='team'),
    path('ClassesTimetable',views.ClassesTimetable,name='classtime'),
    path('BmiCalculator',views.BmiCalculator,name='bmicalculator'),
    path('Gallery',views.Gallery,name='gallery'),
    path('Blog',views.Blog,name='blog'),
    path('BlogDetails',views.BlogDetails,name='blogdetails'),
    path('Contact',views.contact,name='contact'),
   

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)