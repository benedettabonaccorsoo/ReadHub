from django.urls import path
from .views import (
    search_books, home, biblioteca, account, contattaci, notifiche, 
    registrazione, book_list, reserve_book, return_book, login_view, logout_view, request_notification
)

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_books, name='search_books'),
    path('biblioteca/', biblioteca, name='biblioteca'),
    path('account/', account, name='account'),
    path('contattaci/', contattaci, name='contattaci'),
    path('notifiche/', notifiche, name='notifiche'),
    path('registrazione/', registrazione, name='registrazione'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # ✅ Assicurati che sia scritto bene!
    path('books/', book_list, name='book_list'),
    path('reserve/<int:book_id>/', reserve_book, name='reserve_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
    path('notify/<int:book_id>/', request_notification, name='request_notification'),
    path('return/<int:book_id>/', return_book, name='return_book'),

]

