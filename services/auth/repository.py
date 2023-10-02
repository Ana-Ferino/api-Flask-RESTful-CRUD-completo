from models.database.redis.client import KeyValueDBConnection
from config import AppConfig

class AuthSessionRepository:
    def __init__(self) -> None:
        self.db = KeyValueDBConnection()

    def save(self, token: str, usuario: str):
        try:
            two_hours = AppConfig.Redis.time_exp
            self.db.set_value(key=token, value=usuario, expiration=two_hours)
        except Exception as e:
            return e


    def get(self, token: str) -> str:
        try:
            username = self.db.get_value(token)
            return username
        except Exception as e:
            return e