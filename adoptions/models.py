from django.db import models

# Create your models here.
class Pet(models.Model):

    # The list has 2-tuples, one for the DB value, the other for the readable-display value
    SEX_CHOICES = [('M','Male'),('F','Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()

    # Distinction between null and blank, a blank would be recorded as 0, a null is unknown
    age = models.IntegerField(null=True)

    # associate a pet with vaccines.  Some pets may not have vaccinations.
    vaccinations = models.ManyToManyField('Vaccine',blank=True)

# Vaccines has Many-to-many relationships with Pet
class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name