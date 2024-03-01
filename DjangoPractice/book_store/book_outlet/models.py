from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='country'

class Address(models.Model):
    street=models.CharField(max_length=80)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'

    class Meta:
        verbose_name_plural= "Address Entries"


class Author(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,related_name="author",null=True)

    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return self.fullname()


class Book(models.Model):
    title=  models.CharField(max_length=50) #takes string input
    ratings=models.IntegerField() # takes integer input
    # ratings=models.IntegerField(
    #     validators=[MinValueValidator(5),MaxValueValidator(100)])
    #author=models.CharField(null=True, max_length=100)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True,related_name="books")
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(default='',null=False, blank=True, db_index=True)#If title is Harry Potter 1 the slug shld be harry-potter-1 
                                    #editable=False,
    published_countries=models.ManyToManyField(Country)
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])#,kwargs={"pk": self.pk} as replacable arg
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title) #slugs the title field
        super().save(*args,**kwargs) # adds that slug to database

    def __str__(self):
        return f"{self.title} ({self.ratings}) -{self.author}'{self.is_bestselling}'"