from django.urls import path
from .views import user_login,custom_logout,profilview,user_register,edit_profil
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path('login/',user_login,name='login'),
    path('logout/',custom_logout,name='logout'),
    path('profil/',profilview,name='profil'),
    path('password/',PasswordChangeView.as_view(), name='passwordchange'),
    path('passwordone/',PasswordChangeDoneView.as_view(), name="passwordone"),
    path('signup/',user_register,name='signup'),
    path('profiledit/',edit_profil,name='profiledit')
    # path('signup/',SignUpView.as_view(),name='signup')
]
