from django.contrib import admin

# Register your models here.

from .models import Book,Author,Address,Country

class BookAdmin(admin.ModelAdmin):
    #add props or fields that need to be reflected in admin page
    #readonly_fields= ("slug",)
    prepopulated_fields={"slug":("title",)} 
    list_filter=("author","ratings")
    list_display=("title", "author")
 
admin.site.register(Book, BookAdmin)    
admin.site.register(Author)  
admin.site.register(Address)  
admin.site.register(Country)  