from django.db import models


# Create your models here.
class Trainer (models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True, blank=False)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Trainers"

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)


class Activity (models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    dateTime = models.DateTimeField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    activityTrainer = models.ForeignKey(Trainer, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name


class Member (models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True, blank=False)
    lastLogin = models.DateTimeField(auto_now = True)
    image = models.ImageField(max_length = 250, upload_to = "profilePics", default = 'placeholder.jpg')

    activities = models.ManyToManyField(Activity)
    memberTrainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return '%s %s' % (self.firstName, self.lastName)