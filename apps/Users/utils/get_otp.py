import json
import secrets

from redis.exceptions import RedisError
from utils.logging.loggers import redis_logger
from utils.redis_client import redis_client as redis


# function to generate OTP and send it
def get_otp(email):
    otp = ""
    if redis.exists(f"{email}"):
        try:
            otp = redis.get(f"{email}")
        except ConnectionError as error:
            redis_logger.error(f"[ConnectionError] {error}")
        except RedisError as error:
            redis_logger.error(f"[RedisError] {error}")
    else:
        otp = None

    return otp
