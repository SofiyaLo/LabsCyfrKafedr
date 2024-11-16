import json


def task() -> float:
    json_file = 'input.json'
    with open(json_file) as f:
        json_data = json.load(f)

    json_sum = sum([value["score"] * value["weight"] for value in json_data])
    return round(json_sum, 3)


print(task())
