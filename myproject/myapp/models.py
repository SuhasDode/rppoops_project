from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    room  = models.IntegerField(default = 205)
    misno =  models.CharField(max_length=30,default = '612203048')
    collegemailid = models.CharField(max_length=30)
    address =  models.CharField(max_length=150)
    contactno = models.CharField(max_length=20)
    Yearofstudy = models.CharField(max_length=15)
    is_applied = models.BooleanField(default=False)
    mess_token = models.CharField(max_length=150,null=True)
    

class NightAttendence(models.Model):    
    is_marked = models.BooleanField(default=False)
    time = models.DateTimeField(blank=True, null=True, default=None)
    misno = models.CharField(max_length=30,default = '612203048')
    date  =  models.DateTimeField(auto_now_add=True,null=True)
    # You can add any other fields you need for check-in/out details

class laterequest(models.Model):
    misno = models.CharField(max_length=30,default = '612203048')
    date  =  models.DateField(auto_now_add=True,null=True)
    outgoingTime = models.DateTimeField(null=True)
    IncomingTime = models.DateTimeField(null=True)
    is_approved = models.BooleanField(default=False)
    reason = models.CharField(max_length=1000,default = '612203048')

class Meal(models.Model):
    day_of_week = models.CharField(max_length=10,default = 'Mon')
    morning_meal_name = models.CharField(max_length=100,default = 'abc')
    dinner_meal_name = models.CharField(max_length=100,default = 'bcd')
    description = models.CharField(max_length=100,default = 'bcd')
    
class attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    date_of_leave = models.CharField(max_length = 20,default = None)
    is_attending_morning = models.BooleanField(default=True)
    is_attending_night = models.BooleanField(default=True)
    is_penalty=  models.BooleanField(default=False)
    is_penalty_morning=  models.BooleanField(default=False)
    is_penalty_night=  models.BooleanField(default=False)
    month = models.IntegerField(default=0)


class MessBills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    month = models.IntegerField(default = 0)
    bill_status_is_paid = models.BooleanField(default = False)
    bill_amount = models.IntegerField(default=0)
    month_name = models.CharField(max_length = 20,default='abc')
    
# class admin(models.Model):
#     username = models.CharField(max_length = 100)
#     password = models.CharField(max_length = 30)
#     email = models.CharField(max_length = 50)
    


class Complaint(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MaintenanceRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1)  # 1: Low, 2: Medium, 3: High
    resolved = models.BooleanField(default=False)


class LaundryBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    kgs_count = models.PositiveIntegerField()
    service_type = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    booking_date = models.DateField(default=timezone.now)  
    time_slot = models.CharField(max_length=50, default='5:30')  
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.user.username} - {self.booking_date}"

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
