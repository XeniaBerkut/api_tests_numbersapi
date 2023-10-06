import requests

from enums.endpoints import Endpoints


def test_random_interval(logger):
    logger.info('Set numbers interval and check if the random number is in the interval')
    random_interval_endpoint = str(Endpoints.BASE_URL.value) + str(Endpoints.RANDOM.value) + '?min=5&max=5'
    logger.info(f'Go to {random_interval_endpoint}')
    response = requests.get(random_interval_endpoint)
    assert response.status_code == 200
    assert '5' in response.text
