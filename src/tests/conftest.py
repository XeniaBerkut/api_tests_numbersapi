import pytest

from src.endpoints.math_api_endpoint import MathAPIEndpoint
from src.endpoints.submit_api_endpoint import SubmitAPIEndpoint
from src.endpoints.random_api_endpoint import RandomAPIEndpoint


API_BASE_URL = 'http://numbersapi.com'


@pytest.fixture()
def random_endpoint():
    return RandomAPIEndpoint(API_BASE_URL)


@pytest.fixture()
def math_endpoint():
    return MathAPIEndpoint(API_BASE_URL)


@pytest.fixture()
def submit_endpoint():
    return SubmitAPIEndpoint(API_BASE_URL)
