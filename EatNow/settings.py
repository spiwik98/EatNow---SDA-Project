from pathlib import Path
import os

# Katalog główny projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Debugowanie (włączone tylko dla trybu deweloperskiego)
# Podczas rozwijania i testowania aplikacji, ustawienie DEBUG na True jest akceptowalne. W środowisku produkcyjnym zaleca się ustawienie DEBUG na False.
# Ze względu na testowanie aplikacji DEBUG jest ustawiony na TRUE
DEBUG = True

# Klucz używany do generowania tokenów i innych elementów bezpieczeństwa
SECRET_KEY = 'django-insecure-4l*qy%$v351hvmu3yjcejvx*av+hdxz)!vi5^us5@ydivd*g*$'

# Lista hostów, które mogą obsługiwać żądania (w trybie deweloperskim wszystkie)
ALLOWED_HOSTS = []

# cookie CSRF będzie wymagał protokołu HTTPS
CSRF_COOKIE_SECURE = True

# Zabezpieczenie przed niebezpiecznymi nagłówkami
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Zabezpieczenie przed atakami typu Clickjacking
X_FRAME_OPTIONS = 'DENY'

# Zainstalowane aplikacje
INSTALLED_APPS = [
    "pytest",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer',
    'register',
    'crispy_forms',
    'crispy_bootstrap4',
    'django_dump_load_utf8',
]

# Middleware używane przez projekt
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Konfiguracja URL głównego
ROOT_URLCONF = 'EatNow.urls'

# Szablony używane w projekcie
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'EatNow/static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Konfiguracja ASGI (Asynchronous Server Gateway Interface)
WSGI_APPLICATION = 'EatNow.wsgi.application'

# Konfiguracja bazy danych
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eatnow2',
        'USER': 'root',
        'PASSWORD': 'admin',
        'PORT': 3306,
        'HOST': '127.0.0.1',
    }
}

# Konfiguracja walidacji haseł
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Konfiguracja międzynarodowa
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Konfiguracja obsługi plików statycznych
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Konfiguracja backendu email (w trybie deweloperskim wyświetla w konsoli)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Domyślny typ pola klucza głównego
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ustawienia dla aplikacji Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Adres przekierowania po zalogowaniu i wylogowaniu
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'