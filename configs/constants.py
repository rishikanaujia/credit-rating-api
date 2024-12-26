import logging

SERVICE_NAME = "credit_rating_api"
DEFAULT_ENV = "dev"
LOG_TYPE = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "FATAL": logging.FATAL,
}

# log_configs
MAX_LOG_SIZE = 25 * 1024 * 1024
BACKUP_COUNT = 5
