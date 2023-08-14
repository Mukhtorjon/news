from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .form import LoginForm,RegistrationForms,UserEditForm,ProfilEditForm
from newsapp.models import Category,News
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profail


# Create your views 
def user_login(request):
    if request.method == "POST":
        form =LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
                               
            if user is not None:
                if user.is_active:
                    login(request, user)
                
                    return redirect('index')
                else:
                    return HttpResponse("Qayta urining")
            else:
                return HttpResponse('Login yoki Parol xato')
    else:
        form=LoginForm()
        context={'form':form} 
    return render(request,"user.html",context)




@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "qaytadan urining")
    return redirect("index")

def profilview(request):
    user=request.user
    profil=Profail.objects.get(user=user)
    context={'user':user,'profil':profil}
    print(profil)
    return render(request,'profil.html',context)
def user_register(request):
    if request.method=="POST":
        form=RegistrationForms(request.POST)
        if form.is_valid():
            datauser=form.save(commit=False)
            datauser.set_password(form.cleaned_data['password'])
            datauser.save()
            Profail.objects.create(user=datauser)
            context={'form':datauser}
            return render(request,'registertayyor.html',context)
    else:
        form=RegistrationForms()
        context={'form':form}
    return render(request,'register.html',context)
# class SignUpView(CreateView):
#     form_class = RegistrationForms
#     success_url = reverse_lazy('login')
#     template_name = 'register.html'
# class UserPhoto():
def edit_profil(request):
    if request.method=='POST':
        userform=UserEditForm(instance=request.user,data=request.POST)
        profilform=ProfilEditForm(instance=request.user.profail,data=request.POST,files=request.FILES)
        if userform.is_valid() and profilform.is_valid():
            userform.save()
            profilform.save()
    else:
        userform=UserEditForm(instance=request.user)
        profilform=ProfilEditForm(instance=request.user.profail)
    context={'userform':userform,'profilform':profilform} 
    return render(request,'profiledit.html',context)
    