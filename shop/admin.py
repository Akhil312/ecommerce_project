from django.contrib import admin
from . models import category, Product
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    list_per_page= 20
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,productAdmin)

