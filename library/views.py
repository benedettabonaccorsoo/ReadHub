from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Book, Reservation, Notification
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# 📌 Homepage
def home(request):
    return render(request, 'library/ricercalibropiubenvenutmenu.html')

# 📌 Pagina Biblioteca (solo utenti loggati)
@login_required
def biblioteca(request):
    books = Book.objects.all()
    return render(request, 'library/biblioteca1.html', {'books': books})

# 📌 Account Utente
@login_required
def account(request):
    reservations = Reservation.objects.filter(user=request.user)  # 🔍 Recupera le prenotazioni dell'utente attuale
    return render(request, 'library/ilmioaccount.html', {'reservations': reservations})


# 📌 Contatti
def contattaci(request):
    return render(request, 'library/contattaci.html')

# 📌 Notifiche
@login_required
def notifiche(request):
    notifications = Notification.objects.filter(user=request.user, seen=False)
    return render(request, 'library/notifiche.html', {'notifications': notifications})

# 📌 Lista dei Libri
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# 📌 Prenotazione Libro
@login_required
def reserve_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available:
        book.available = False
        book.save()
        Reservation.objects.create(user=request.user, book=book)
        messages.success(request, f"Hai prenotato il libro: {book.title}")

        # Rimuove le notifiche perché il libro è stato prenotato
        Notification.objects.filter(book=book).delete()
    else:
        messages.error(request, f"Il libro '{book.title}' è già prenotato!")

    return redirect('search_books')


    

# 📌 Registrazione Utente
def registrazione(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']  # ✅ Sistemato errore di sintassi

        # Controlla se l'email è già registrata
        if User.objects.filter(username=email).exists():
            return render(request, 'library/reg1.1.html', {'error': 'Email già registrata!'})

        # Crea il nuovo utente
        user = User.objects.create_user(
            username=email, first_name=first_name, last_name=last_name, email=email, password=password
        )
        user.save()

        # Login automatico dopo la registrazione
        login(request, user)  
        return redirect('home')  # Dopo la registrazione, reindirizza alla home
        
    return render(request, 'library/reg1.1.html')

# 📌 Login Utente
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # Se avevi un "next" nella querystring, puoi reindirizzare lì:
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)  # Oppure: return redirect('home')
        else:
            # Mostra un messaggio di errore
            return render(request, 'library/login.html', {'error': 'Email o password errati!'})
    
    # Se GET, mostro il form di login senza errori
    return render(request, 'library/login.html')


# 📌 Logout Utente
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # ✅ Reindirizza alla home dopo il logout

# 📌 Ricerca Libri
def search_books(request):
    query_title = request.GET.get('title', '')  
    query_author = request.GET.get('author', '')
    query_category = request.GET.get('category', '')
    books = Book.objects.all()
    
    if query_title:
        books = books.filter(title__icontains=query_title)
    if query_author:
        books = books.filter(author__icontains=query_author)
    if query_category:
        books = books.filter(genre__icontains=query_category)

    return render(request, 'library/search_results.html', {'books': books})

from .models import Notification

@login_required
def request_notification(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Notification.objects.create(user=request.user, book=book)
    messages.success(request, f"Riceverai una notifica quando '{book.title}' sarà disponibile.")
    return redirect('search_books')

@login_required
def return_book(request, book_id):
    # Trova il libro e la prenotazione corrispondente
    book = get_object_or_404(Book, id=book_id)
    reservation = Reservation.objects.filter(user=request.user, book=book).first()

    if reservation:
        # Rendi il libro nuovamente disponibile
        book.available = True
        book.save()

        # Cancella la prenotazione
        reservation.delete()

        messages.success(request, f"Hai restituito il libro: {book.title}")

    return redirect('account')  # Torna alla pagina "Il mio Account"

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Trova la prenotazione attiva per questo utente e libro
    reservation = Reservation.objects.filter(user=request.user, book=book).first()
    
    if reservation:
        book.available = True  # Rendi il libro nuovamente disponibile
        book.save()
        reservation.delete()  # Rimuovi la prenotazione
        messages.success(request, f"Hai restituito il libro: {book.title}")
    else:
        messages.error(request, "Nessuna prenotazione trovata per questo libro.")
    
    return redirect('account')  # Torna alla pagina account

