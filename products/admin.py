from django.contrib import admin
from .models import product
# admin.site.register(product)

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=('name','price','image')
admin.site.register(product,productadmin)
