import requests
from bs4 import BeautifulSoup

from .settings import settings


class Utils():
    """Class for the valid links determination"""

    @staticmethod
    def get_valid_pages():

        valid = []
        for i in range(165):
            print(i)
            r = requests.get(settings.link, params={"id": i})
            soup = BeautifulSoup(r.text, 'html.parser')

            if len([x.get_text().strip() for x in soup.find_all(class_="right_l")]) == 6:
                if "Профиль этого динозавра ещё не был создан." not in \
                        [x.get_text().strip() for x in soup.find_all(class_="gray_text")][0]:
                    valid.append(str(i))

        with open("valid.txt", "w") as f:
            f.write(",".join(valid))


if __name__ == '__main__':
    Utils.get_valid_pages()
