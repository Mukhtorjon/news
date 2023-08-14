from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name



class News(models.Model):
    CHOICES = (
        ('Qora', 'Qoralama'),
        ('Tay', 'Tayyor'),
       
    )
    title=models.CharField(max_length= 200)
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    image=models.ImageField(upload_to='static/img',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    publik_time=models.TimeField()
    create_time=models.TimeField()
    update_time=models.TimeField()
    status = models.CharField(max_length=300, choices = CHOICES)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("new", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
    
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    message=models.TextField()
    def __str__(self):
        return self.email
  