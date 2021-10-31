import logging
import os

import bot


class Settings():
    """Setting for the project"""

    link = "http://dinopedia.ru"
    info_add_link = "/dinosaur.php"
    API_TOKEN = '2087623412:AAF22z5PCaYTlTOVIeP9hvfxMrcFpHFMkEA'
    log_level = logging.INFO
    project_path = os.path.dirname(bot.__file__)


settings = Settings()
