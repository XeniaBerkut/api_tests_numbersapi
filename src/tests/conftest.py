import pytest

from endpoints.math_api_endpoint import MathAPIEndpoint
from endpoints.submit_api_endpoint import SubmitAPIEndpoint
from src.endpoints.random_api_endpoint import RandomAPIEndpoint


@pytest.fixture()
def random_endpoint():
    return RandomAPIEndpoint()


@pytest.fixture()
def math_endpoint():
    return MathAPIEndpoint()


@pytest.fixture()
def submit_endpoint():
    return SubmitAPIEndpoint()
