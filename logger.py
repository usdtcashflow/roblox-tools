import logging
from logging.handlers import RotatingFileHandler

# Configure logger settings
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'roblox_tool.log'
LOG_MAX_SIZE = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 3

# Initialize logger
logger = logging.getLogger('RobloxTool')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Add handler to logger
logger.addHandler(handler)

if __name__ == '__main__':
    logger.info('Logger setup complete')
