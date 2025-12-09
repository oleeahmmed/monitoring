from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime

# ১. কোম্পানি মডেল (Multi-Company সাপোর্টের জন্য)
class Company(models.Model):
    name = models.CharField(max_length=200)
    company_code = models.CharField(max_length=50, unique=True) # লগিনের সময় লাগতে পারে
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ২. এমপ্লয়ি প্রোফাইল (User এর সাথে Company কে লিঙ্ক করা)
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"

# ডাইনামিক ফোল্ডার পাথ জেনারেটর (Company/User/Date অনুযায়ী ফোল্ডার হবে)
def screenshot_upload_path(instance, filename):
    company_name = instance.employee.company.name.replace(" ", "_")
    username = instance.employee.user.username
    date_str = datetime.now().strftime("%Y-%m-%d")
    return f"screenshots/{company_name}/{username}/{date_str}/{filename}"

# ৩. স্ক্রিনশট মডেল
class Screenshot(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to=screenshot_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # অতিরিক্ত তথ্য (যদি দরকার হয়)
    screen_index = models.IntegerField(default=1) # কোন মনিটরের ছবি

    def __str__(self):
        return f"Shot: {self.employee.user.username} at {self.created_at}"
