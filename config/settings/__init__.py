from decouple import config

ENVIRONMENT = config("DJANGO_ENV", default="dev")

if ENVIRONMENT == "prod":
    from .prod import *  # noqa: F401,F403
else:
    from .dev import *  # noqa: F401,F403
