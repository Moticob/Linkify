# Linkify: URL Shortener Application

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Django](https://img.shields.io/badge/Django-4.0+-green.svg) ![OAuth 2.0](https://img.shields.io/badge/OAuth-2.0-red.svg) ![Google](https://img.shields.io/badge/Google-OAuth2-blue.svg) ![SQL](https://img.shields.io/badge/SQL-Supported-brightgreen.svg)

Welcome to **Linkify**, a URL shortener application built using Django and the `pyshorteners` package. This project also includes OAuth 2.0 authentication with Google.

## Features

- **URL Shortening**: Convert long URLs into short, manageable links.
- **OAuth 2.0 with Google**: Secure authentication using Google accounts.
- **Django Framework**: Robust backend with Django, ensuring scalability and maintainability.
- **Bootstrap UI**: A clean and responsive user interface built with Bootstrap.

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- pyshorteners
- A Google Cloud project with OAuth 2.0 credentials

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/linkify.git
    cd linkify
    ```

2. **Install dependencies**:
    ```bash
    pip install django pyshorteners
    ```

3. **Set up the Django project**:
    ```bash
    django-admin startproject linkify
    cd linkify
    python3 manage.py startapp main
    ```

4. **Configure the application**:
    - Register the `main` app in `linkify/settings.py`:
        ```python
        INSTALLED_APPS = [
           ...
           'main.apps.MainConfig',
           ...
        ]
        ```

## Google OAuth 2.0 Integration

1. **Set up OAuth credentials**:
    - Create OAuth 2.0 credentials in the Google Cloud Console.
    - Download the credentials JSON file and place it in your project directory.

2. **Configure Django settings**:
    - Update `linkify/settings.py` with your OAuth credentials:
        ```python
        SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-client-id>'
        SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-client-secret>'
        ```

## Usage

### Run the Server

Start the Django development server:

```bash
python manage.py runserver
```

## Access the Application

Navigate to http://127.0.0.1:8000 in your web browser to use Linkify.

## API Documentation
```
Endpoints
Shorten URL
Endpoint: /shorten/
Method: POST
Request Body:
json
Copier le code
{
    "url": "http://example.com/very/long/url"
}
Response:
json
Copier le code
{
    "short_url": "http://short.url/xyz123"
}
Description: Converts a long URL into a short URL.
Expand URL
Endpoint: /expand/
Method: POST
Request Body:
json
Copier le code
{
    "short_url": "http://short.url/xyz123"
}
Response:
json
Copier le code
{
    "url": "http://example.com/very/long/url"
}
Description: Expands a short URL back into the original long URL.

Authentication
Endpoint: /auth/
Method: GET
Description: Initiates the OAuth 2.0 authentication process with Google.
Project Structure

linkify/
├── main/
│   ├── templates/
│   │   └── url-shortener.html
│   ├── views.py
│   ├── urls.py
├── linkify/
│   ├── settings.py
│   ├── urls.py
URL Shortener Logic
The core logic for shortening URLs is implemented in the url_shortener view function in main/views.py:

python
Copier le code
# main/views.py

from django.shortcuts import render
import pyshorteners
from django.contrib import messages

def url_shortener(request):
    try:
        short_url = ""
        url = ""
        if request.method == "POST":
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
        return render(
            request, "url-shortener.html", {"short_url": short_url, "url": url}
        )
    except:
        return render(request, "url-shortener.html")
```
## Contributions
Feel free to fork this repository and contribute via pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Contact
For any queries or suggestions, reach out to me at oussama.ed-derouach@outlook.com.
