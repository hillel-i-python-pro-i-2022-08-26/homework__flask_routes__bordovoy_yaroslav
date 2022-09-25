"""
Считывание файла
PATH: /requirements/
Возвращать содержимое файла. Любой текстовый файл.
"""

from function_store import path_settings


def path_txt():
    ROOT_PATH = path_settings.ROOT_PATH_txt
    FILES_PATH_txt = ROOT_PATH.joinpath("requirements.txt")
    return FILES_PATH_txt


def read_requirements():
    requirements_file = path_txt()
    with open(requirements_file) as file:
        return file.read()


if __name__ == "__main__":
    read_requirements()
