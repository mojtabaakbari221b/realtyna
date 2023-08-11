from .base import * #NOSONAR

DEBUG=False

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
    'rest_framework.renderers.JSONRenderer',
]

CORS_ORIGIN_ALLOW_ALL = False
