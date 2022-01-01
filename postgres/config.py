from backend.constants import Connections


TORTOISE_ORM = {
    "connections": {"default": Connections.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["postgres.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}