"""
Logger getting foo
"""
import logging


def get_logger(name: str) -> logging.Logger:
    """Get default logger by name

    Args:
        name (str): name of logger

    Returns:
        logging.Logger: logger
    """
    logger = logging.getLogger(name)
    return logger
