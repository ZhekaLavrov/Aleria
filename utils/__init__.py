import psycopg2

import config


def create_connection():
    """
    Создает подключение к базе данных используя переменные из config.py.
    :return: Объект подключения
    """
    connection = psycopg2.connect(
        user=config.DataBase.USER,
        password=config.DataBase.PASSWORD,
        host=config.DataBase.HOST,
        port=config.DataBase.PORT,
        database=config.DataBase.DATABASE
    )
    return connection
