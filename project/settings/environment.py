import os
from pathlib import Path

from utils.environment import get_env_variable, parse_comma_sep_str_to_list

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'INSECURE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') == '1' else False

ALLOWED_HOSTS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('ALLOWED_HOSTS')
)
CSRF_TRUSTED_ORIGINS: list[str] = parse_comma_sep_str_to_list(
    get_env_variable('CSRF_TRUSTED_ORIGINS')
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # noqa
    'PAGE_SIZE': 10,
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cadastrosraposos@gmail.com'
EMAIL_HOST_PASSWORD = '6pel2018'


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
