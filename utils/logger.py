import logging
import os
from logging.handlers import RotatingFileHandler

from configs.constants import MAX_LOG_SIZE, BACKUP_COUNT, SERVICE_NAME


def setup_logger(name, log_file=None, level=logging.INFO, max_log_size=MAX_LOG_SIZE, backup_count=BACKUP_COUNT):
    """Function to configure and return a logger with rotating file handler and stream handler."""

    # Create log directory in the root of the project
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # If log_file is provided, ensure it is within the log directory
    if log_file:
        log_file_path = os.path.join(log_dir, log_file)
    else:
        log_file_path = os.path.join(log_dir, f'{SERVICE_NAME}.log')

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler with rotating log file (max size 25 MB and keep 5 backup files)
    rotating_handler = RotatingFileHandler(log_file_path, maxBytes=max_log_size, backupCount=backup_count)
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)

    # Stream handler (for console output)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


# Initialize the logger for the project with log rotation
project_logger = setup_logger(name=SERVICE_NAME, log_file=f'{SERVICE_NAME}.log')
