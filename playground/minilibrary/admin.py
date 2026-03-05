from webbrowser import get

from django.contrib import admin
from .models import Author, Genre, Book, BookDetail, Review, Loan, Recommendation 
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

User = get_user_model()

admin.site.site_header = "Mini Biblioteca Admin"
admin.site.site_title = "Mini Biblioteca Admin Portal"
admin.site.index_title = "Bienvenido al panel de administración de la Mini Biblioteca"

@admin.action(description='Marcar como devuelto')
def mark_as_returned(modeladmin, request, queryset):
    queryset.update(is_returned=True)
    modeladmin.message_user(request, f"{queryset.count()} préstamos marcados como devueltos.")

class LoanInline(admin.TabularInline):
    model = Loan
    extra = 0
    verbose_name_plural = 'Préstamos'
    

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    
class BookDetailInline(admin.StackedInline):
    model = BookDetail
    can_delete = False
    verbose_name_plural = 'Detalle del libro'

class CustomUserAdmin(BaseUserAdmin):
    inlines = [LoanInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ["name"]
    list_filter = ('birth_date',)
    ordering = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, BookDetailInline]
    list_display = ('title', 'author','pages', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('published_date', 'genres', 'author')
    ordering = ['published_date']
    date_hierarchy = 'published_date'
    filter_horizontal = ('genres',)
    readonly_fields = ('pages',)
    autocomplete_fields = ['author', 'genres']
    fieldsets = (
        ("Informacion general", {
            'fields': ('title', 'author', 'published_date', 'genres')
        }),
        ("Detalles adicionales", {
            'fields': ('pages', 'isbn'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj = None):
        return request.user.is_staff

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'loan_date', 'return_date', 'is_returned')
    search_fields = ('book__title', 'user__username')
    list_filter = ('is_returned', 'loan_date', 'return_date')
    date_hierarchy = 'loan_date'
    readonly_fields = ('loan_date',)
    actions = [mark_as_returned]
    raw_id_fields = ['book', 'user']

# admin.site.register(Author)
# admin.site.register(Genre)
admin.site.register(BookDetail)
admin.site.register(Review)
admin.site.register(Recommendation)

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, CustomUserAdmin)