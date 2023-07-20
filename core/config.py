"""
Environment requirements:

    Flask:
        DEBUG
            type: int | None
            default: 0
            description:
                0 - False
                1 - True
"""

from os import environ, getenv, sep
from pathlib import Path
from environs import Env

__all__ = ["Config"]

env = Env()
env.read_env()


class Config:
    BASE_DIR = str(Path(__file__).resolve().parent.parent).replace(sep, "/")
    DEBUG_MODE = env.bool("DEBUG", default=False)

    SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SWAGGER_FORMS = BASE_DIR + "/swagger_forms/"
    UPLOAD_FOLDER = BASE_DIR + "/media/"

