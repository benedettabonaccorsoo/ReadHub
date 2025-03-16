from django.db import models
from django.contrib.auth.models import User

# 📌 Modello per i Libri
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    available = models.BooleanField(default=True)  # Indica se il libro è disponibile

    def __str__(self):
        return self.title

# 📌 Modello per le Prenotazioni
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ha prenotato {self.book.title}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']  # Ordina le notifiche dalla più recente alla più vecchia
  

    def __str__(self):
        return f"Notifica per {self.user.username} - {self.book.title}"

