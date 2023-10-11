import logging
import pytest
import requests
import test_data


@pytest.mark.parametrize("test_case",
                         test_data.data_random_number_in_interval,
                         ids=[data["test_case_title"] for data in test_data.data_random_number_in_interval])
def test_random_number_in_interval(test_case: dict, random_endpoint):
    """ Check if we have correct status code and the number in the response for random interval """

    logging.info('Set numbers interval and check if the random number is in the interval')
    interval = test_case["data"]
    random_interval_endpoint = random_endpoint.build_url_with_interval(interval)
    logging.info(f'Get {random_interval_endpoint}')
    response = requests.get(random_interval_endpoint)
    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert random_endpoint.number_in_interval(response.text, interval), (f'Expected text about number in {interval}, '
                                                                         f'but was text: {response.text}')


@pytest.mark.parametrize("test_case",
                         test_data.data_random_number_in_rational_interval,
                         ids=[data["test_case_title"] for data in test_data.data_random_number_in_rational_interval])
def test_random_number_in_rational_interval(test_case: dict, random_endpoint):
    """ Check if we have correct status code and the number in the response for rational interval """

    logging.info('Set rational interval and check if the random number is in the interval')
    interval = test_case["data"]
    random_interval_endpoint = random_endpoint.build_url_with_interval(interval)
    logging.info(f'Get {random_interval_endpoint}')
    response = requests.get(random_interval_endpoint)
    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert random_endpoint.number_in_rational_interval(response.text, interval), \
        f'Expected text about number in {interval}, but was text: {response.text}'


def test_random_words_instead_of_numbers(random_endpoint, data=test_data.data_random_words_instead_of_numbers):
    """ Check if we have correct status and random number in the response when words are used as an interval """

    logging.info('Set words as interval boundaries and check if we receive a random number')
    interval = data
    random_interval_endpoint = random_endpoint.build_url_with_interval(interval)
    logging.info(f'Get {random_interval_endpoint}')
    response = requests.get(random_interval_endpoint)
    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert random_endpoint.is_random_number(response.text), \
        f'Expected text about number in {interval}, but was text: {response.text}'


def test_random_number_min_more_than_max(random_endpoint, interval=test_data.data_random_number_min_more_than_max):
    """Check if we have correct status code, no number and correct message in the response """

    logging.info('Set min parameter more than max in url and check that no number will be returned')
    url = random_endpoint.build_url_with_interval(interval)
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status_code 200 for url {url}, but received {response.status_code}"
    with pytest.raises(ValueError):
        random_number = int(response.text.split()[0])
    assert 'undefined is' in response.text


@pytest.mark.parametrize("test_case",
                         test_data.data_get_math_fact,
                         ids=[data["test_case_title"] for data in test_data.data_get_math_fact])
def test_get_math_fact(test_case: dict, math_endpoint):
    """ Check if we have correct status code and the number in the response for specified number """

    number = str(test_case["number"])
    logging.info(f'Get number {number} and specify an url')

    number_url = math_endpoint.build_number_url(number)
    logging.info(f'Get {number_url}')
    response = requests.get(number_url)

    assert response.status_code == 200, f'Expected status_code 200, but was {response.status_code}'
    assert math_endpoint.is_correct_number_in_response(response.text, number), (f'Expected fact about {number}, '
                                                                                f'but was text: {response.text}')


def test_get_math_fact_rational_number(math_endpoint, number=test_data.data_get_math_fact_rational):
    """ Check if we have correct status code and message in the response when specify rational number """
    number_url = math_endpoint.build_number_url(number)
    logging.info(f'Get {number_url}')
    response = requests.get(number_url)

    assert response.status_code == 400, f'Expected status_code 400, but was {response.status_code}'
    assert response.text == 'Invalid url', f'Expected "Invalid url" but was text: {response.text}'


def test_submit_new_fact(submit_endpoint, data=test_data.data_post_submit_new_fact):
    """ Check if we have correct status code and empty message in the response """
    logging.info(f'Send a new fact about {data["number"]}')
    response = requests.post(submit_endpoint.endpoint_url, json=data)

    assert response.status_code == 200, f'Expected status code 200 but was {response}'
    assert submit_endpoint.is_empty_response_content(response.content)


def test_submit_new_fact_bad_request_wrong_host(submit_endpoint, data=test_data.data_post_submit_bad_request):
    """ Check if we have correct status code and message in the response when request wrong host """
    logging.info(f'Send a new fact about {data["body"]["number"]}')
    response = requests.post(submit_endpoint.endpoint_url, headers=data["headers"], json=data)

    assert response.status_code == 400, f'Expected status code 400 but was {response}'
    assert response.reason == 'Bad Request', f'Expected "Bad Request", but was {response.reason}'
