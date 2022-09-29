import pathlib


ROOT_PATH = pathlib.Path(__file__).parents[1]
FILES_PATH_txt = ROOT_PATH.joinpath("requirements.txt")

ROOT_PATH_csv = pathlib.Path("./function_store/flask_functions/")
FILES_PATH_csv = ROOT_PATH_csv.joinpath("people_data.csv")

DB_PATH = ROOT_PATH.joinpath("database_sql", "db.sqlite")
