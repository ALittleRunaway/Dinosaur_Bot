import re
from random import randint
from unicodedata import normalize

import requests
from bs4 import BeautifulSoup

from .settings import settings


class Dinosaur:
    """The dinosaur class"""

    def __init__(self):
        self.name = None
        self.height = None
        self.length = None
        self.weight = None
        self.ration = None
        self.found = None
        self.similar = None
        self.description = None
        self.img = None
        self.link = None

    def get_info(self):
        """Parses the website to find the appropriate information"""

        with open(f"{settings.project_path}/valid.txt", "r") as f:
            ids = f.read().split(",")

        r = requests.get(f"{settings.link}{settings.info_add_link}", params={"id": ids[randint(0, len(ids))]})
        soup = BeautifulSoup(r.text, 'html.parser')

        self.link = r.url

        self.name = re.sub(
            r'\s+', ' ', normalize("NFKD", " ".join(x.get_text().strip() for x in soup.find_all(class_="ru_title"))))

        self.height, self.length, self.weight, self.ration, self.found, self.similar = \
            [re.sub(r'\s+', ' ', normalize("NFKD", x.get_text().strip())) for x in soup.find_all(class_="right_l")]

        self.img = f"{settings.link}/{[x['src'] for x in soup.find_all('img') if x['src'].endswith('logo.jpg')][0]}"

        self.description = "".join(
            [normalize("NFKD", x.get_text().strip()) for x in soup.find_all(class_="gray_text")
             if "Научная классификация" not in x.get_text().strip() and ".." not in x.get_text().strip()])

    def create_media_message(self):
        """Creates an image message reply"""

        message = f"""
🦖 {self.name} 🦖
        
Рост: {self.height}
Длина: {self.length}
Вес: {self.weight}
Питание: {self.ration}
Обнаружен: {self.found}
Похожие ископаемые: {self.similar}

{self.link}
        """
        return message

    def create_description_message(self):
        """Creates a text message reply"""

        message = f"""
{self.description}
        """
        return message


if __name__ == '__main__':
    ds = Dinosaur()
    ds.get_info()
