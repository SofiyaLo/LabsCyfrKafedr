import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_data:
        row_list = [row for row in csv.DictReader(csv_data)]

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(row_list, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


