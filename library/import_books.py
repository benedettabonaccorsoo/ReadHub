import csv
from library.models import Book

def import_books_from_csv():
    with open('books.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Book.objects.create(
                title=row['Title'],
                author=row['Author'],
                genre=row['Genre'],
                available=True  # Imposta tutti i libri come disponibili all'inizio
            )
    print("✅ Importazione completata con successo!")


