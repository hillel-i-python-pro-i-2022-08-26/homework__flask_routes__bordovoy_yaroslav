import pathlib


def read_txt():
    ROOT_PATH = pathlib.Path(__file__).parents[1]
    FILES_PATH_txt = ROOT_PATH.joinpath("requirements.txt")

    return FILES_PATH_txt


def read_csv():
    ROOT_PATH = pathlib.Path(__file__).parents[0]
    FILES_PATH_csv = ROOT_PATH.joinpath("people_data.csv")

    return FILES_PATH_csv
