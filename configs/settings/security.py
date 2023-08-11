from ..utility import load_env

env = load_env()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

SECURE_PROXY_SSL_HEADER = (
    env('HTTP_X_FORWARDED_PROTO'),
    'https',
)

CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

USE_X_FORWARDED_HOST = True