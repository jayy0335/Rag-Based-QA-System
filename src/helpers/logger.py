import logging
import traceback

# Configure the logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to handler
ch.setFormatter(formatter)

# Add handler to logger
logger.addHandler(ch)

# Helper functions with traceback info
def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)

def error(message):
    logger.error(message)

def exception(exc):
    # Log exception with traceback
    tb_str = ''.join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    logger.error(f"Exception occurred: {exc}\nTraceback:\n{tb_str}")

def debug(message):
    logger.debug(message)