from django.db import models

# Create your models here.
class Project(models.Model):
  project_name = models.CharField(max_length=280)
  project_description = models.TextField(null=True, blank=True)
  start_date = models.DateField()
  end_date = models.DateField(null=True, blank=True)
  isactive = models.BooleanField()

  def __str__(self):
    return self.project_name

class Category(models.Model):
  category_name = models.CharField(max_length=280)
  category_description = models.TextField(null=True, blank=True)
  isactive = models.BooleanField(default=True)

  def __str__(self):
    return self.category_name

class Entry(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  hours = models.DecimalField(max_digits=7, decimal_places=2)
  rate = models.DecimalField(max_digits=7, decimal_places=2)
  dollars = models.DecimalField(max_digits=11, decimal_places=2)
  record_date = models.DateField()

