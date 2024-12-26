import configparser
import os
from typing import Dict, Any
from flask import Flask

# Default environment if not set
from configs.constants import DEFAULT_ENV

# Load the configuration from an .ini file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.ini")
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Determine the current environment
ENV = os.environ.get("FLASK_ENV", DEFAULT_ENV)


class Config:
    """Central configuration class for Flask application settings."""

    def __init__(self):
        # General Flask Configurations
        self.ENV = os.getenv("FLASK_ENV", config.get(ENV, "env", fallback="dev"))
        self.DEBUG = os.getenv("DEBUG", config.getboolean(ENV, "debug", fallback=False))
        self.HOST = os.getenv("HOST", config.get(ENV, "host", fallback="127.0.0.1"))
        self.PORT = os.getenv("PORT", config.getint(ENV, "port", fallback=5000))
        self.LOGGING_TYPE = os.getenv("LOGGING_TYPE", config.get(ENV, "logging_type", fallback="ERROR"))

        # Application-Specific Configurations

        # Optional Configurations (add more as needed)
        self.CACHE_TYPE = os.getenv("CACHE_TYPE", config.get(ENV, "cache_type", fallback="simple"))

    def as_dict(self) -> Dict[str, Any]:
        """Returns configuration as a dictionary for debugging or external usage."""
        return self.__dict__


def apply_config_to_app(app: Flask):
    """
    Apply the loaded configuration to a Flask application instance.

    :param app: Flask application object
    :return: None
    """
    cfg = Config()
    for key, value in cfg.as_dict().items():
        app.config[key] = value
