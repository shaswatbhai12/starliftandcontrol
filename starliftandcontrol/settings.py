import os
from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '851d-122-177-111-70.ngrok-free.app', 
    'localhost', 
    '127.0.0.1',
    '4766-122-177-107-88.ngrok-free.app',
    '4d5e-106-215-90-88.ngrok-free.app',
    'e2f1-122-177-104-92.ngrok-free.app',
    'bold-blowfish-uniformly.ngrok-free.app',
    'starliftandcontroller.xyz', 
    'www.starliftandcontroller.xyz',
    'https://starliftandcontrol.vercel.app/',
    '.vercel.app',
    '.onrender.com', # This allows Render's internal health checks
    '.starliftandcontroller.xyz'
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",  # Ensure your 'home' app is listed here
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add this right here!
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Only keep this one
    "home.middleware.AllowNgrokInFrameMiddleware",  # Add your custom middleware here
    

]

# Set X-Frame-Options to SAMEORIGIN (recommended)
X_FRAME_OPTIONS = 'SAMEORIGIN'  # This will allow your site to be embedded only within the same origin

# Uncomment the below line if you want to allow embedding from your specific ngrok URL
# X_FRAME_OPTIONS = 'ALLOW-FROM https://851d-122-177-111-70.ngrok-free.app'

ROOT_URLCONF = "starliftandcontrol.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates/home'],  # Ensure this directory exists
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "starliftandcontrol.wsgi.application"

# Database Configuration (SQLite by default)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://851d-122-177-111-70.ngrok-free.app",
    "https://bold-blowfish-uniformly.ngrok-free.app",
    "https://starliftandcontroller.xyz", 
    "https://www.starliftandcontroller.xyz",
    "https://*.onrender.com", # Added https:// and a wildcard *
    "https://*.starliftandcontroller.xyz", # Added https:// and a wildcard *

]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"  # Example for India
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Ensure this directory exists
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (for user-uploaded content like images)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

import mimetypes
mimetypes.add_type("text/css", ".css", True)

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'shaswatkumar9868@gmail.com'

