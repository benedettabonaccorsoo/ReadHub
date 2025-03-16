# ReadHub - Online Library Management System

ReadHub is an online library management system developed with Django. It allows users to search for books, make reservations, and receive notifications about book availability.
# Features
User Registration & Authentication: Secure login and registration system.
Book Search & Filters: Users can search books by title, author, or genre.
Reservation System: Users can reserve books if available or request notifications when unavailable.
Notifications: Alerts users when reserved books become available.
User Account Management: Users can view and manage their reservations.
Admin Interface: A built-in Django admin panel for managing users and books.

 Installation & Setup
1️⃣ Prerequisites
Make sure you have the following installed on your system:

Python (recommended version 3.10 or higher)
Git
Virtual environment (optional but recommended)
SQLite (included with Django)
2️⃣ Clone the Repository
git clone https://github.com/benedettabonaccorso/ReadHub.git
cd ReadHub
3️⃣ Create and Activate a Virtual Environment
# Create virtual environment
python3 -m venv myenv

# Activate the virtual environment
# On macOS/Linux:
source myenv/bin/activate
# On Windows (Command Prompt):
myenv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Apply Migrations & Setup Database
python3 manage.py migrate
6️⃣ Create a Superuser (Optional for Admin Access)
python3 manage.py createsuperuser
Follow the prompts to create an admin account.

7️⃣ Run the Development Server
python3 manage.py runserver
The project will be accessible at:
🔗 http://127.0.0.1:8000/

# How to Use the Application
Visit the homepage and browse the book catalog.
Register/Login to access your personal dashboard.
Search for books using the search bar and filters.
Reserve books if available or request notifications when unavailable.
Manage reservations from the "My Account" section.
Admin users can log in to http://127.0.0.1:8000/admin/ to manage books and users.

