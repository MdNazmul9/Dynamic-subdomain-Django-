from django.contrib import admin

# Register your models here.
from  .models import  Tanent, Member

admin.site.register(Tanent)
admin.site.register(Member)