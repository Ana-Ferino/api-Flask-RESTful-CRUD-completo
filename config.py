from dotenv import load_dotenv

load_dotenv('.env')

class AppConfig:

    class SecretsToken:
        secret_key = load_dotenv('SECRECT_KEY_TOKEN')