import logging
from logging.handlers import RotatingFileHandler

from .settings import settings


class Logger:
    """The local custom logger"""

    @staticmethod
    def get_logger():
        """Creates the logger"""

        log_formatter = logging.Formatter('%(asctime)s  ::  %(levelname)-8s  ::  %(message)s')

        my_handler = RotatingFileHandler(f"{settings.project_path}/logs.log",
                                         maxBytes=1024 * 1024, backupCount=1, encoding="utf-8")
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(settings.log_level)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        logger.addHandler(my_handler)

        return logger
