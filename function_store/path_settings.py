import pathlib
from typing import Final


ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
PATH_TO_REQUIREMENT_FILE: Final[pathlib.Path] = ROOT_PATH.joinpath("requirements.txt")

PATH_TO_FILES: Final[pathlib.Path] = pathlib.Path("function_store", "flask_functions")
PATH_TO_PEOPLE_DATA_CSV: Final[pathlib.Path] = PATH_TO_FILES.joinpath("people_data.csv")

DB_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath("database_sql", "db.sqlite")
