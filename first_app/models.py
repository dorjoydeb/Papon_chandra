from django.db import models


class Proj_cate(models.Model):
    Category_name = models.CharField(max_length=100, blank=False, default=None)

    def __str__(self):
        return self.Category_name


class Projects(models.Model):
    Select_category = models.ForeignKey(Proj_cate, on_delete=models.CASCADE, default=None)
    Image_Url = models.URLField(max_length=1000, blank=False, default=None)
    Url = models.URLField(max_length=500, blank=True)
    Title = models.CharField(max_length=30, blank=True)
    Sub_title = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.Title


class Email_info(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(max_length=50, blank=False)
    Subject = models.CharField(max_length=100, blank=True)
    Phone = models.IntegerField(blank=True, default=None)
    Message = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.Name
# Create your models here.
