import os

from enums.endpoints import Endpoints
from src.endpoints.random import Random
import pytest
import requests
from src.helpers.test_data_helpers import get_test_data_from_json

data_random_interval = get_test_data_from_json(os.path.join(
    os.path.dirname(__file__),
    "test_random_interval_data.json"))


@pytest.mark.parametrize("test_case",
                         data_random_interval,
                         ids=[data["test_case_title"] for data in data_random_interval])
def test_get_random_interval(logger, test_case: dict):
    logger.info('Set numbers interval and check if the random number is in the interval')
    random_endpoint = Random(logger)
    interval = test_case["data"]
    random_interval_endpoint = random_endpoint.set_url_with_interval(interval)
    logger.info(f'Get {random_interval_endpoint}')
    response = requests.get(random_interval_endpoint)
    assert response.status_code == 200
    assert random_endpoint.number_in_interval(response.text, interval)


def test_post_submit(logger):
    logger.info('Add a new fact')

    headers = {}

    data = {
        "text": "zbvbzxc",
        "number": "26",
        "type": "trivia"
    }

    response = requests.post(Endpoints.MATH.value, headers=headers, json=data)
    assert response.status_code == 200, f'Expected status 404 OK but was {response}'


def test_put_math(logger):
    logger.info('Try to PUT to math endpoint')

    data = {
        "id": 1001,
        "number": 1001,
        "odd": True
    }

    response = requests.put(Endpoints.MATH.value, json=data)
    assert response.status_code == 404, f'Expected status 404 OK but was {response}'


def test_patch_math(logger):
    logger.info('Try to patch to math endpoint')

    data = {
        "odd": False
    }

    response = requests.put(Endpoints.MATH.value, json=data)
    assert response.status_code == 404, f'Expected status 404 OK but was {response}'
