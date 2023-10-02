from dotenv import load_dotenv
import os

load_dotenv('.env')

class AppConfig:

    class SecretsToken:
        SECRET_KEY = os.getenv('SECRECT_KEY_TOKEN')

    class Redis:
        host = os.getenv('REDIS_HOST')
        port = os.getenv('REDIS_PORT')
        user = os.getenv('REDIS_USER')
        db = os.getenv('REDIS_DB')
        password = os.getenv('REDIS_PW')
        time_exp = os.getenv('TIME_EXP_TOKEN_IN_REDIS')