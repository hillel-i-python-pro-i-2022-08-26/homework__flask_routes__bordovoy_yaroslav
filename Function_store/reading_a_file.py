"""
Считывание файла
PATH: /requirements/
Возвращать содержимое файла. Любой текстовый файл.
"""

import pathlib


ROOT_PATH = pathlib.Path(__file__).parents[1]
FILES_PATH = ROOT_PATH.joinpath("requirements.txt")


def read_requirements():

    with open(FILES_PATH) as file:
        return file.read()


if __name__ == "__main__":
    read_requirements()
