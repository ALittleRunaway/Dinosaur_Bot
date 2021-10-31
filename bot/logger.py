import logging

from .settings import settings


class Logger:
    """The local custom logger"""

    @staticmethod
    def get_logger():
        """Creates the logger"""

        logging.basicConfig(format='%(asctime)s ::  %(levelname)-8s :: %(message)s', level=settings.log_level)
        logger = logging.getLogger(__name__)

        return logger
