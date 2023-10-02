from config import AppConfig
from typing import Union
import redis


class KeyValueDBConnection:
    def __init__(self, config=AppConfig.Redis):
        self.redis_connection = redis.Redis(
            host=config.host,
            port=config.port,
            charset="utf-8",
            decode_responses=True
        )
    
    def get_value(self, key: str) -> Union[str, None]:
        value = self.redis_connection.get(key)
        if value is None:
            return None

        return value
    
    def set_value(self, key: str, value: str, expiration: float = None):
        self.redis_connection.set(key, value, ex=expiration)

    def get_dict(self, key: str) -> dict:
        redis_dict = self.redis_connection.hgetall(key)
        decoded_dict = {k.decode('utf8'): v.decode('utf8') for k, v in redis_dict.items()}

        return decoded_dict

    def set_dict(self, key: str, properties_dict: dict):
        self.redis_connection.hmset(key, properties_dict)
    
    def get_all_keys(self) -> list[str]:
        keys = self.redis_connection.keys()

        return keys