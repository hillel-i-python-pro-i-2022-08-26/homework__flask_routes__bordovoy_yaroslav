from flask import Flask

from function_store import reading_a_file, user_generator, space_astro, average_data

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
    iss_list = []
    ship_list = []
    for i in num_astro["people"]:
        if i["craft"] == "ISS":
            iss_list.append(i["name"])
        else:
            ship_list.append(i["name"])
    return (
        f'<p>Astronauts at the moment: {num_astro["number"]}</p>'
        f'<p>ISS crafting: {", ".join(iss_list)}</p>'
        f'<p>Tiangong crafting: {", ".join(ship_list)}</p>'
    )


# PATH: /mean/
@app.route("/mean")
def mean() -> str:
    return f"{average_data.average()}"


if __name__ == "__main__":
    app.run(debug=True)
