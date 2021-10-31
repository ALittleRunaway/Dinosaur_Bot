import os

import bot


class Settings():
    """Setting for the project"""

    link = "http://dinopedia.ru"
    info_add_link = "/dinosaur.php"
    log_level = "INFO"
    project_path = os.path.dirname(bot.__file__)


settings = Settings()
