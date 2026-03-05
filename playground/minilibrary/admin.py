from django.contrib import admin
from .models import Author, Genre, Book, BookDetail, Review, Loan, Recommendation 

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','pages', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('published_date', 'genres', 'author')
    ordering = ['published_date']
    date_hierarchy = 'published_date'
    filter_horizontal = ('genres',)

admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail)
admin.site.register(Review)
admin.site.register(Loan)
admin.site.register(Recommendation)