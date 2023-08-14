from django.urls import path
from .views import myblog5,contact,mynew3,Edit_write,Delete_s,Creat_News,Newsapp

urlpatterns = [

    path('',Newsapp.as_view(),name='index'),
    # path('new/<slug:slug>',Myblog5.as_view(),name='new'),
    path('new/<slug:slug>',myblog5,name='new'),
    path('contact/',contact,name='contact'),
    path('mynew3/',mynew3,name='404'),
    path('edit/<slug:slug>',Edit_write.as_view(),name='edit'),
    path('delete/<slug:slug>',Delete_s.as_view(),name='delete'),
    path('create/',Creat_News.as_view(),name='create')                                     
  
   
  
  


]