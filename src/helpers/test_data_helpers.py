import json
import os


def get_test_data_from_json(test_data_file_name: str) -> dict:
    json_path = os.path.abspath(test_data_file_name)
    if "src" not in json_path:
        json_path = os.path.abspath('src/tests/' + test_data_file_name)
    with open(json_path, "r") as json_file:
        test_data = json.load(json_file)
    return test_data
