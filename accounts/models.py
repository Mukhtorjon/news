from django.db import models
from newsapp.models import News
from django.contrib.auth.models import User
# Create your models here.
class Profail(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="static/user_photo/",blank=True,null=True)
    manzil=models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
 
    def __str__(self):
        return f'{self.user.username} shu profili'
class Comment(models.Model):
    profil=models.ForeignKey(Profail,
                            on_delete=models.CASCADE,
                            related_name='comments')
    news=models.ForeignKey(News,
                           on_delete=models.CASCADE,
                           related_name='comments')
    user=models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='comments')
    body=models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    
    class Mate:
        ordering=['-create_time']