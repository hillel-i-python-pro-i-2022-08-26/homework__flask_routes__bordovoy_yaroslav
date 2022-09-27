"""
Считывание файла
PATH: /requirements/
Возвращать содержимое файла. Любой текстовый файл.
"""

from function_store.path_settings import FILES_PATH_txt


def read_requirements():
    with open(FILES_PATH_txt) as file:
        return file.read()


if __name__ == "__main__":
    read_requirements()
