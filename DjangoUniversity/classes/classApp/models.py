# title charfield
# #course number integer field
# #intructor charfield
# #duration float field
# from django.db import models

from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField(default=0)
    instructor = models.CharField(max_length=60,blank=True)
    duration = models.FloatField()
    classes = models.Manager()




