from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=250)
    website=models.URLField(max_length=100)
    
    def __str__(self):
        return f'{self.name}' 

class Watchlist(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.CharField(max_length=250)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    avg_rating=models.FloatField(default=0)
    count_rating=models.IntegerField(default=0)
    
    
    def __str__(self):
        return f'{self.title}'
    
class Review(models.Model):
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    watchlist=models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name='reviews')
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.watchlist} {"|"} {self.rating}'

# class Movie(models.Model):
#     name=models.CharField(max_length=50)
#     description=models.CharField(max_length=300)
#     active=models.BooleanField(default=True)
    
#     def __str__(self):
#         return f'{self.name} {self.description}' 
    
#     class Meta:
#         verbose_name_plural='Movie_Title'
        
