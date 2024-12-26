import configparser
import os
from typing import Dict, Any
from flask import Flask
from configs.constants import (
    DEFAULT_ENV,
    CONFIG_FILE_NAME,
    ENV_KEY,
    DEBUG_KEY,
    HOST_KEY,
    PORT_KEY,
    LOGGING_TYPE_KEY,
    CACHE_TYPE_KEY,
    DEFAULT_CONFIG_VALUES,
)

# Load the configuration from an .ini file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), CONFIG_FILE_NAME)
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Determine the current environment
ENV = os.environ.get(ENV_KEY, DEFAULT_ENV)


class Config:
    """Central configuration class for Flask application settings."""

    def __init__(self):
        # General Flask Configurations
        self.ENV = os.getenv(ENV_KEY, config.get(ENV, ENV_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[ENV_KEY]))
        self.DEBUG = os.getenv(DEBUG_KEY, config.getboolean(ENV, DEBUG_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[DEBUG_KEY]))
        self.HOST = os.getenv(HOST_KEY, config.get(ENV, HOST_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[HOST_KEY]))
        self.PORT = os.getenv(PORT_KEY, config.getint(ENV, PORT_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[PORT_KEY]))
        self.LOGGING_TYPE = os.getenv(
            LOGGING_TYPE_KEY, config.get(ENV, LOGGING_TYPE_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[LOGGING_TYPE_KEY])
        )

        # Application-Specific Configurations
        self.CACHE_TYPE = os.getenv(
            CACHE_TYPE_KEY, config.get(ENV, CACHE_TYPE_KEY.lower(), fallback=DEFAULT_CONFIG_VALUES[CACHE_TYPE_KEY])
        )

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
