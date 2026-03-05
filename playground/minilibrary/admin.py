from django.contrib import admin
from .models import Author, Genre, Book, BookDetail, Review, Loan, Recommendation 

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','pages', 'published_date')
    search_fields = ('title', 'author__name')

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail)
admin.site.register(Review)
admin.site.register(Loan)
admin.site.register(Recommendation)