import logging


class MathAPIEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_number_url(self, number: str) -> str:
        """ Build url for specified number to get a math fact"""

        number_url = f'{self.base_url}/{number}/math'
        logging.info(f'Number URL = {number_url}')
        return number_url

    @staticmethod
    def is_correct_number_in_response(text: str, number: str) -> bool:
        """ Check if specified number is in the response text """
        logging.info(f'Check if {number} is in response text')
        return number in text
