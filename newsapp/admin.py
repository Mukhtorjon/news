from django.contrib import admin
from .models import Category,News,Contact
admin.site.register(Category)
admin.site.register(Contact)
# admin.site.register(News)


# Register your models here.
@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display=[ 'id','title','slug', 'publik_time', 'status' ]
    list_filter=[ 'status', 'create_time', 'publik_time' ]
    prepopulated_fields={'slug':('title',)}
    search_fields=[ 'title']

    