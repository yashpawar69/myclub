# MyClub

MyClub is a Django-based web application for managing club events and venues. It allows users to create, view, update, and delete event information, manage venues, search for venues, and handle member authentication via login and registration.

## Features

- Event management
  - Add, view, update, and delete events
  - Track event dates and descriptions
  - Associate events with venues and managers
- Venue management
  - Add venues with address, city, contact details, and website information
  - Search for venues
  - List and view individual venue details
  - Export venue data in text, CSV, or PDF formats
- Member access
  - User registration
  - Login/logout support
  - Admin access for club management
- Media support
  - Venue image uploads
- Django admin integration
  - Manage data via the built-in admin panel

## Tech Stack

- Python
- Django 4.2
- SQLite (default database)
- HTML templates
- Django forms and models
- Pillow for image uploads

## Project Structure

```text
myclub/
├── myclub_web/
│   ├── events/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── members/
│   │   ├── templates/
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── myclub_web/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── media/
└── .gitignore
```

## Prerequisites

Before running the app, make sure you have:

- Python 3.10+
- pip
- virtualenv (recommended)

## Installation

1. Clone the repository

```bash
git clone https://github.com/yashpawar69/myclub.git
cd myclub
```

2. Create and activate a virtual environment

```bash
cd myclub_web
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies

```bash
pip install django pillow
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Then open the app in your browser at:

```text
http://127.0.0.1:8000/
```

## Admin Access

To access the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials created above.

## Usage

- Visit the home page to browse club events
- Navigate to venue-related pages to add or manage venues
- Use the login/register pages to access member features
- Use the admin dashboard to manage event and venue records

## Environment Notes

This project currently uses SQLite as the default database, which is suitable for local development and testing.

## Contributing

Contributions are welcome. If you want to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project does not currently include a license file. If this repository is intended for public use, it is recommended to add an appropriate open-source license such as MIT.

## Author

Yash Pawar
