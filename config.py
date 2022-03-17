import os

TELEGRAM_BOT_TOKEN = os.getenv("ALERIA_CHAT_BOT_TELEGRAM_TOKEN")


class DataBase:
    USER = os.getenv("ALERIA_DATABASE_USER")
    PASSWORD = os.getenv("ALERIA_DATABASE_PASSWORD")
    HOST = os.getenv("ALERIA_DATABASE_HOST")
    PORT = os.getenv("ALERIA_DATABASE_PORT")
    DATABASE = os.getenv("ALERIA_DATABASE_DB")
