import os

from endpoints.math import Math
from endpoints.submit import Submit
from enums.endpoints import Endpoints
from src.endpoints.random import Random
import pytest
import requests
from src.helpers.test_data_helpers import get_test_data_from_json

data_random_interval = get_test_data_from_json("test_data/data_get_random_interval.json")


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
    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert random_endpoint.number_in_interval(response.text, interval), (f'Expected text about number in {interval}, '
                                                                         f'but was text: {response.text}')


data_get_math_fact = get_test_data_from_json("test_data/data_get_math_facts.json")


@pytest.mark.parametrize("test_case",
                         data_get_math_fact,
                         ids=[data["test_case_title"] for data in data_get_math_fact])
def test_get_math_fact(logger, test_case: dict):
    logger.info('Get number and specify an url')
    number = str(test_case["number"])
    math_endpoint = Math(logger, number)

    logger.info(f'Get {math_endpoint.number_url}')
    response = requests.get(math_endpoint.number_url)

    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert math_endpoint.is_correct_number_in_response(response.text, number), (f'Expected fact about {number}, '
                                                                 f'but was text: {response.text}')


def test_post_submit_new_fact(logger):
    logger.info("Get test data for request")
    # data = get_test_data_from_json(os.path.join(os.path.dirname(__file__), "data_post_submit_new_fact.json"))
    data = get_test_data_from_json("test_data/data_post_submit_new_fact.json")

    logger.info(f'Send a new fact about {data["body"]["number"]}')
    response = requests.post(Endpoints.SUBMIT.value, headers=data["headers"], json=data["body"])

    submit_endpoint = Submit(logger)
    assert response.status_code == 200, f'Expected status code 200 but was {response}'
    assert submit_endpoint.is_empty_response_content(response.content)
