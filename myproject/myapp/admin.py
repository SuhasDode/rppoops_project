from django.contrib import admin
# Register your models here.
from myapp.models import Meal,attendance,student,NightAttendence,laterequest

admin.site.register(Meal)
admin.site.register(attendance)
admin.site.register(student)
admin.site.register(NightAttendence)
admin.site.register(laterequest)