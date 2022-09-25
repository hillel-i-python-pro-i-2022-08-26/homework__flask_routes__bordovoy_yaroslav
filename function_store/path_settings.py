import pathlib


ROOT_PATH_txt = pathlib.Path(__file__).parents[1]
FILES_PATH_txt = ROOT_PATH_txt.joinpath("requirements.txt")

ROOT_PATH_csv = pathlib.Path(__file__).parents[0]
FILES_PATH_csv = ROOT_PATH_csv.joinpath("people_data.csv")
