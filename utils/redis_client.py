# from django.conf import settings
from redis import Redis
from project.settings import CELERY_BROKER_URL
import redis
from utils.logging.loggers import redis_logger

redis_client = None


try:
    pool = redis.ConnectionPool.from_url(CELERY_BROKER_URL)

    with Redis(connection_pool=pool) as client:
        redis_client = client
except Exception as error:
    redis_client = None
    redis_logger.error(f"[Exception] {error}")