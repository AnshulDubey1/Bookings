from redis import Redis
from core.config import settings

redis_client =Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    decode_responses=True
)

def get_redis():
    return redis_client