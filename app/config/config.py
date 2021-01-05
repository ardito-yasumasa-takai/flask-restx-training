import os

from sqlalchemy.engine.url import URL


class DatabaseConfig:

    DATABASE_URI = URL(
        drivername="mysql+pymysql",
        username=os.getenv("DB_MYSQL_USER"),
        password=os.getenv("DB_MYSQL_PASSWORD"),
        host=os.getenv("DB_MYSQL_HOST"),
        database=os.getenv("DB_MYSQL_DATABASE"),
        port=os.getenv("DB_MYSQL_PORT") or None,
        query={"charset": "utf8"},
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DatabaseConfig
