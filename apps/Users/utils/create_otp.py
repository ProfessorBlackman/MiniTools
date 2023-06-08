import json
import secrets

from redis.exceptions import RedisError
from utils.logging.loggers import redis_logger
from utils.redis_client import redis_client as redis


# function to generate OTP and send it
def create_otp(email):
    otp = f"{secrets.token_hex(6)}"
    # save otp to redis
    try:
        redis.set(f"{email}", json.dumps(otp), ex=3600)
    except ConnectionError as error:
        redis_logger.error(f"[ConnectionError] {error}")
    except RedisError as error:
        redis_logger.error(f"[RedisError] {error}")

    return otp
