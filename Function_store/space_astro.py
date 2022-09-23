"""
Вывести количество космонавтов в настоящий момент.
Можно вывести как минимум просто цифру с результатом. Можно добавить ещё
текст, описывающий смысл этой цифры.
При желании, можно также вывести дополнительную информацию.
Что явно запрещено, так это просто выводить полученный JSON. Нужно его
обработать, взять нужные данные и передать на вывод.
"""

import json

import requests


def get_astro():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    text_json = response.text
    ready_json = json.loads(text_json)

    return ready_json


if __name__ == "__main__":
    get_astro()
