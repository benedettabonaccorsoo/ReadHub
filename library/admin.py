from django.contrib import admin
from .models import Book, Reservation  # Importiamo i modelli

# ✅ Aggiungiamo i Libri all'admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')  # Mostra questi campi nella lista
    list_filter = ('available',)  # Filtro per Disponibile/Non Disponibile
    search_fields = ('title', 'author')  # Permette di cercare per Titolo o Autore

# ✅ Aggiungiamo le Prenotazioni all'admin
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'date_reserved')  # Mostra questi campi
    list_filter = ('date_reserved',)  # Filtro per Data di Prenotazione
    search_fields = ('user__username', 'book__title')  # Permette di cercare per Utente o Titolo Libro

