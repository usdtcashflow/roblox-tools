import logging

class Logger:
    """Custom logger for the application."""

    def __init__(self, name='roblox-tools'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Create console handler and set level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        # Add the handlers to the logger
        self.logger.addHandler(ch)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)

# Example usage
if __name__ == '__main__':
    log = Logger()
    log.info('This is an info message.')
    log.error('This is an error message.')