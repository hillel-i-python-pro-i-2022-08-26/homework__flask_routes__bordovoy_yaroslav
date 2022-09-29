from flask import Flask, Response
from webargs import fields
from webargs.flaskparser import use_args

from function_store.db_foo.creating_sql_table import create_table
from function_store.db_foo.db_connection import DBConnection
from function_store.flask_foo import (
    average_data,
    space_astro,
    user_generator,
    reading_a_file,
)

app = Flask(__name__)


# Homepage
@app.route("/")
def hello() -> str:
    return "Hello, this is flask homework!"


# PATH: /requirements/
@app.route("/requirements")
def read_file() -> str:
    return "".join(
        f"<p>{str}</p>" for str in reading_a_file.read_requirements().split("\n")
    )


# PATH: /generate-users/
@app.route("/generate-users")
@app.route("/generate-users/<int:amount>")
def generate_users(amount: int = 100) -> str:
    for user in range(amount):
        user += 1
        yield "".join(f"<ol>{user}: {user_generator.generate_fake_user()}</ol>")


# PATH: /space/
@app.route("/space")
def space() -> str:
    num_astro = space_astro.get_astro()
    yield f'<p>Astronauts at the moment: {num_astro["number"]}</p><br>'
    for name in num_astro["people"]:
        yield f'<p>{name["name"]} is part of the {name["craft"]} group</p>'


# PATH: /mean/
@app.route("/mean")
def mean() -> str:
    return f"{average_data.average()}"


# Database SQlite
create_table()


@app.route("/phones/create")
@use_args(
    {
        "contact_name": fields.Str(required=True),
        "phone_value": fields.Int(required=True),
    },
    location="query",
)
def db_phones_create(args):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (:contact_name, :phone_value)",
                {
                    "contact_name": args["contact_name"],
                    "phone_value": args["phone_value"],
                },
            )

    return "Data entered"


@app.route("/phones/read-all")
def db_phones_read_all():
    with DBConnection() as connection:
        names_from_table = connection.execute("SELECT * FROM phones;").fetchall()

    return "<br>".join(
        [
            f"{names['phone_ID']}: {names['contact_name']} --- {names['phone_value']}"
            for names in names_from_table
        ]
    )


@app.route("/phones/read-user/<int:phone_ID>")
def db_phones_read_user(phone_ID: int):
    with DBConnection() as connection:
        user = connection.execute(
            "SELECT * FROM phones WHERE (phone_ID=:phone_ID);",
            {"phone_ID": phone_ID},
        ).fetchone()

        if user is None:
            return f"Sorry, user ID {phone_ID} does not exist"

    return f'{user["phone_ID"]}: {user["contact_name"]} - {user["phone_value"]}'


@app.route("/phones/update/<int:phone_ID>")
@use_args({"contact_name": fields.Str(), "phone_value": fields.Int()}, location="query")
def db_phones_update(args, phone_ID: int):
    with DBConnection() as connection:
        with connection:
            contact_name = args.get("contact_name")
            phone_value = args.get("phone_value")
            if contact_name is None and phone_value is None:
                return Response("Sorry, you dont provide any value", status=400)

            args_for_request = []
            if contact_name is not None:
                args_for_request.append("contact_name=:contact_name")
            if phone_value is not None:
                args_for_request.append("phone_value=:phone_value")

            args_str = ", ".join(args_for_request)

            connection.execute(
                f"UPDATE phones SET {args_str} WHERE (phone_ID=:phone_ID);",
                {
                    "phone_ID": phone_ID,
                    "contact_name": contact_name,
                    "phone_value": phone_value,
                },
            )
    return f"User ID {phone_ID} data changed"


@app.route("/phones/delete/<int:phone_ID>")
def db_phones_delete(phone_ID):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "DELETE FROM phones WHERE (phone_ID=:phone_ID);", {"phone_ID": phone_ID}
            )

    return f"User ID {phone_ID} deleted"


if __name__ == "__main__":
    app.run(debug=True)
