"""
Считывание файла
PATH: /requirements/
Возвращать содержимое файла. Любой текстовый файл.
"""

from function_store.path_settings import PATH_TO_REQUIREMENT_FILE


def read_requirements():
    with open(PATH_TO_REQUIREMENT_FILE) as file:
        return file.read()


if __name__ == "__main__":
    read_requirements()
