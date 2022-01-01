from decouple import config


class Connections:
    DATABASE_URL = config("DATABASE_URL")
