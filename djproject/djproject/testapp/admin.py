from django.contrib import admin
from testapp.models import Hydjobs,Blorejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class BlorejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Hydjobs, HydjobsAdmin)
admin.site.register(Blorejobs,BlorejobsAdmin)

