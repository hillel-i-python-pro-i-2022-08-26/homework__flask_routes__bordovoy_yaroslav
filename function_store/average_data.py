import csv

from function_store.path_settings import FILES_PATH_csv


def average():
    with open(FILES_PATH_csv, newline="") as file:
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
    average()
