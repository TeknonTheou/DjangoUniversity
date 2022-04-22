from django.contrib import admin
#import DjangoClasses model
from .models import DjangoClasses
#register DjangoClasses model for admin access
admin.site.register(DjangoClasses)
