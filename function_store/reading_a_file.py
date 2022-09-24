"""
Считывание файла
PATH: /requirements/
Возвращать содержимое файла. Любой текстовый файл.
"""

from function_store import path_settings


def read_requirements():
    new_path = path_settings.read_txt()
    with open(new_path) as file:
        return file.read()


if __name__ == "__main__":
    read_requirements()
