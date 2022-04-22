from django.db import models

#define model and attributes


class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default=0, blank=True)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default=0.00)

    objects = models.Manager()

    def __str__(self):
        return self.Title
