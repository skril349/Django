# ────────────────────────────────
# 0. Imports y utilidades
# ────────────────────────────────
import random
import itertools
from datetime import date, timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

from minilibrary.models import (
    Author, Genre, Book, BookDetail,
    Review, Loan, Recommendation
)

User = get_user_model()

# ────────────────────────────────
# 1. Usuarios (20)
# ────────────────────────────────
users = []

for i in range(1, 21):
    user, created = User.objects.get_or_create(
        username=f"user{i}",
        defaults={"email": f"user{i}@demo.com"}
    )

    if created:
        user.set_password("pass1234")
        user.save()

    users.append(user)

# ────────────────────────────────
# 2. Autores (20)
# ────────────────────────────────
authors = []

for i in range(1, 21):
    author, _ = Author.objects.get_or_create(
        name=f"Autor {i}",
        defaults={"birth_date": date(1950 + i, 1, 1)}
    )
    authors.append(author)

# ────────────────────────────────
# 3. Géneros (20)
# ────────────────────────────────
genre_names = [
    "Ficción", "Drama", "Ciencia Ficción", "Distopía",
    "Aventura", "Romance", "Misterio", "Histórico",
    "Poesía", "Fantástico", "Biografía", "Ensayo",
    "Horror", "Thriller", "Policíaco", "Humor",
    "Infantil", "Juvenil", "Filosofía", "Autoayuda"
]

genres = []

for name in genre_names:
    genre, _ = Genre.objects.get_or_create(name=name)
    genres.append(genre)

# ────────────────────────────────
# 4. Libros (20)
# ────────────────────────────────
books = []

for i in range(1, 21):

    book, created = Book.objects.get_or_create(
        isbn=f"ISBN-{1000+i}",
        defaults={
            "title": f"Libro {i}",
            "published_date": date(2000 + i, 6, 1),
            "author": random.choice(authors),
            "pages": random.randint(150, 600)
        }
    )

    # Asignar géneros (ManyToMany)
    book.genres.set(random.sample(genres, 2))

    books.append(book)

# ────────────────────────────────
# 5. BookDetail (1 por libro)
# ────────────────────────────────
for book in books:

    BookDetail.objects.get_or_create(
        book=book,
        defaults={
            "summary": f"Resumen de {book.title}",
            "cover_url": f"https://picsum.photos/seed/{book.id}/200/300",
            "language": random.choice(["Español", "Inglés", "Francés"])
        }
    )

# ────────────────────────────────
# 6. Reviews (20)
# ────────────────────────────────
for i in range(20):

    Review.objects.create(
        user=random.choice(users),
        book=random.choice(books),
        rating=random.randint(1, 5),
        text="Excelente lectura" if i % 2 == 0 else "Interesante pero mejorable"
    )

# ────────────────────────────────
# 7. Loans (20)
# ────────────────────────────────
today = timezone.now()

for i in range(20):

    loan_date = today - timedelta(days=random.randint(1, 60))
    returned = i % 2 == 0

    Loan.objects.create(
        user=random.choice(users),
        book=random.choice(books),
        loan_date=loan_date,
        is_returned=returned,
        return_date=loan_date + timedelta(days=15) if returned else None
    )

# ────────────────────────────────
# 8. Recommendations (20)
# ────────────────────────────────
book_cycle = itertools.cycle(books)

for i in range(20):

    Recommendation.objects.create(
        user=random.choice(users),
        book=next(book_cycle),
        note="¡Tienes que leerlo!"
    )

print("✅ Seed completado correctamente.")