from rest_framework import serializers
from .models import Screenshot, Employee

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['image', 'screen_index', 'created_at']

    def create(self, validated_data):
        # রিকোয়েস্ট পাঠানো ইউজার থেকেই এমপ্লয়ি বের করা হবে
        user = self.context['request'].user
        try:
            employee = user.employee_profile
            return Screenshot.objects.create(employee=employee, **validated_data)
        except Employee.DoesNotExist:
            raise serializers.ValidationError("User is not assigned to any company/employee profile.")