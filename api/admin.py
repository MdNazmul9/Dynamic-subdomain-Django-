from django.contrib import admin

# Register your models here.
from  .models import  Institute, Member

admin.site.register(Institute)
admin.site.register(Member)