import logging

SERVICE_NAME = "credit_rating_api"

# Default environment settings
DEFAULT_ENV = "dev"

# Configuration file name
CONFIG_FILE_NAME = "config.ini"

# Configuration keys
ENV_KEY = "FLASK_ENV"
DEBUG_KEY = "DEBUG"
HOST_KEY = "HOST"
PORT_KEY = "PORT"
LOGGING_TYPE_KEY = "LOGGING_TYPE"
CACHE_TYPE_KEY = "CACHE_TYPE"

# Default values for configuration keys
DEFAULT_CONFIG_VALUES = {
    ENV_KEY: "dev",
    DEBUG_KEY: False,
    HOST_KEY: "127.0.0.1",
    PORT_KEY: 5000,
    LOGGING_TYPE_KEY: "ERROR",
    CACHE_TYPE_KEY: "simple",
}

LOG_TYPE = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR,
    "FATAL": logging.FATAL,
}

# log_configs
MAX_LOG_SIZE = 25 * 1024 * 1024
BACKUP_COUNT = 5

# Constants for Loan-to-Value Risk
LTV_HIGH_THRESHOLD = 0.9
LTV_MEDIUM_THRESHOLD = 0.8
LTV_HIGH_SCORE = 2
LTV_MEDIUM_SCORE = 1
LTV_LOW_SCORE = 0

# Constants for Debt-to-Income Risk
DTI_HIGH_THRESHOLD = 50
DTI_MEDIUM_THRESHOLD = 40
DTI_HIGH_SCORE = 2
DTI_MEDIUM_SCORE = 1
DTI_LOW_SCORE = 0

# Constants for Credit Score Risk
CREDIT_SCORE_GOOD = 700
CREDIT_SCORE_POOR = 650
CREDIT_SCORE_GOOD_DEDUCTION = -1
CREDIT_SCORE_POOR_ADDITION = 1
CREDIT_SCORE_NEUTRAL = 0

# Constants for Loan Type Risk
LOAN_TYPE_FIXED = "fixed"
LOAN_TYPE_ADJUSTABLE = "adjustable"
LOAN_TYPE_FIXED_SCORE = -1
LOAN_TYPE_ADJUSTABLE_SCORE = 1

# Constants for Property Type Risk
PROPERTY_TYPE_SINGLE_FAMILY = "single_family"
PROPERTY_TYPE_CONDO = "condo"
PROPERTY_TYPE_SINGLE_FAMILY_SCORE = 0
PROPERTY_TYPE_CONDO_SCORE = 1

# Constants for Final Credit Rating
RATING_SCORE_AAA = 2
RATING_SCORE_BBB = 5
RATING_AAA = "AAA"
RATING_BBB = "BBB"
RATING_C = "C"



