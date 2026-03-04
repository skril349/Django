from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null = True, blank = True)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(null = True, blank = True)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=50, unique=True)
    genres = models.ManyToManyField(Genre, related_name='books')
    
    def __str__(self):
        return self.title
    
class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='detail')
    summary = models.TextField()
    language = models.CharField(max_length=50)
    cover_url = models.CharField(max_length=200, null=True, blank=True)    
    def __str__(self):
        return f"Details of {self.book.title}"
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title} ({self.rating}/5)"
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.loan_date}"