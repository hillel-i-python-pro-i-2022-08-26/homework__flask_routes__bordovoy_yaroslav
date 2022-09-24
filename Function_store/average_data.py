import csv
import pathlib


ROOT_PATH = pathlib.Path(__file__).parents[0]
FILES_PATH = ROOT_PATH.joinpath("people_data.csv")


def average():
    with open(FILES_PATH, newline="") as file:
        reader = csv.DictReader(file)
        average_height = 0
        average_weight = 0
        row_counter = 0
        for row in reader:
            average_height += float(row[' "Height(Inches)"'])
            average_weight += float(row[' "Weight(Pounds)"'])
            row_counter += 1

        return (
            f"<p>Average height is: {round(average_height / row_counter, 2)} kg</p>"
            f"<p>Average weight is: {round(average_weight / row_counter, 2)} cm</p>"
        )


if __name__ == "__main__":
    print(average())
