from django.db import models
from django.utils import timezone

from information.models import CourseDetail


class References(models.Model):
    name = models.CharField(max_length=100)


class Status(models.Model):
    status = models.CharField(max_length=100)


class Course(CourseDetail):

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    reference = models.ForeignKey(References, on_delete=models.CASCADE, related_name="enquries")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="enquries")
    date = models.DateField(default=timezone.now)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enquries")
    remark = models.CharField(max_length=100, blank=True, null=True)


class FollowUp(models.Model):
    enquiry_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE, related_name="followups")
    scheduled_time = models.TimeField()
    scheduled_date = models.DateField()
    is_acknowledged = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)
