from django.contrib import admin
from .models import Quotes
# Register your models here.
@admin.register(Quotes)
class DisplayQuotes(admin.ModelAdmin):
    list_display = ['id','quote','author']