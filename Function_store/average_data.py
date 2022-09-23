import csv


def average():
    with open("people_data.csv", newline="") as file:
        reader = csv.DictReader(file)
        average_height = 0
        average_weight = 0
        row_counter = 0
        for row in reader:
            average_height += float(row[' "Height(Inches)"'])
            average_weight += float(row[' "Weight(Pounds)"'])
            row_counter += 1

        return (
            f"Average height is: {round(average_height / row_counter, 2)} kg"
            f"Average weight is: {round(average_weight / row_counter, 2)} cm"
        )


if __name__ == "__main__":
    print(average())
