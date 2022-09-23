"""
Сгенерировать данные пользователей и вывести на страницу.
Формат данных: "Vasya example@mail.com"
По умолчанию, пусть будет 100 пользователей. Добавить опциональный параметр, который регулирует
количество пользователей.
"""

from faker import Faker


fake = Faker()


def generate_fake_users():
    name = fake.first_name()
    email = fake.domain_name()
    return f"{name}@{email}"


if __name__ == "__main__":
    generate_fake_users()
