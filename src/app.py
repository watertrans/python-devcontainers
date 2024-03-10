import logging
import sys
import os

def setup_logger():
    """
    This function sets and returns the logger.
    """

    # WARNING and lower level logs are output to stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.NOTSET)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)

    # ERROR and CRITICAL level logs are output to stderr
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)

    logger = logging.getLogger('Python DevContainers')

    # The log output level can be controlled by environment variables. The default and invalid value is INFO.
    log_level_str = os.getenv("LOG_LEVEL", "INFO")
    log_level = getattr(logging, log_level_str.upper(), None)
    if not isinstance(log_level, int):
        log_level = logging.INFO
    logger.setLevel(log_level)
    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)

    return logger

logger = setup_logger()

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

