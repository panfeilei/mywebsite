from django.apps import AppConfig
import redis
from django.core.cache import cache

class UsersConfig(AppConfig):
    name = 'users'
    conn = redis.Redis('12.55.565.9',6851)
    cache.set()
