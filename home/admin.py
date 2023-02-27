from django.contrib import admin
from .models import departments, jobs, login
# Register your models here.

admin.site.register(departments)
admin.site.register(jobs)

class loginadmin(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Email_address','Logged_on')
admin.site.register(login, loginadmin)
