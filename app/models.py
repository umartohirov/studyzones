from django.db import models



class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

class Place(models.Model):
    STATUSS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    seats = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    opening_hours = models.CharField(max_length=300, null=True, blank=True)
    contact = models.CharField(max_length=30, null=True, blank=True)
    rating = models.CharField(max_length=100, null=True, choices=RATING)
    agreement = models.CharField(max_length=100, choices=STATUSS)

    def __str__(self):
        return self.name




