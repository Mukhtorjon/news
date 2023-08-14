from django.shortcuts import render,get_object_or_404
from .models import Category,News
from django.views.generic import UpdateView,ListView,DeleteView,CreateView,DetailView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from accounts.form import CommentForm
from accounts.models import Profail



# Create your views here.
class Newsapp(ListView):
    model=News
    context_object_name="News"
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
        context['Last_news'] = News.objects.all().order_by("-create_time")[:5]
        context['Maxaliy_news'] = News.objects.filter(category__name="Mahaliy").order_by("-create_time")
        context['Xorij_news'] = News.objects.filter(category__name="Jahon").order_by("-create_time")
        context['Texno_news'] = News.objects.filter(category__name="Texnalogiya").order_by("-create_time")
        context['iqtisod'] = News.objects.filter(category__name="Iqtisodiy").order_by("-create_time")
        return context

def contact(request):
    form=ContactForm(request.POST or None)
    if request.method=='POST' and form.is_valid:
        form.save()
        
        return HttpResponse("xabar jo'natildi")
    context={'form':form}
    return render(request, template_name='contact.html',context=context)

# class Myblog5(DetailView):
#     model=News
#     template_name='single_page.html'
#     context_object_name='new'
#     new=News.objects.all()
def myblog5(request,slug):
    news=get_object_or_404(News,slug=slug)
    context={}
    profil=Profail.objects.get(user=request.user)
    comments=news.comments.filter(active=True)
    newcomment=None
    if request.method=='POST':
        commentsform=CommentForm(data=request.POST)
        if commentsform.is_valid():
           profil=Profail.objects.get(user=request.user)
           newcomment=commentsform.save(commit=False)
           newcomment.news=news
           newcomment.profil=profil
           newcomment.user=request.user
           newcomment.save()
           commentsform=CommentForm()
           return HttpResponseRedirect(slug)
    else:
        
      commentsform=CommentForm()
    context= {'new1':news,'comments':comments,'newcomment':newcomment,'commentsform':commentsform,}
    return render(request,'single_page.html',context)
        
   



def mynew3(request):
    return render(request=request,template_name="404.html")

class Edit_write(UpdateView):
    model=News
    template_name="edit.html"
    context_object_name='News'
    fields=('title','body','image','category')
class Delete_s(DeleteView):
    model=News
    template_name='delete.html'           
    fields=reverse_lazy("index")
class Creat_News(CreateView):
    model=News
    template_name='createnews.html'
    fields=('image','body','title','category','publik_time','status','create_time','update_time')


  
    
    
    
    
    '''+79912913855 gulnoza'''