import logging


class RandomAPIEndpoint:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoint_url = f'{self.base_url}/random'

    @staticmethod
    def number_in_interval(response_text: str, interval: dict):
        """ Check if random number is within the specified interval"""
        logging.info("Get number")
        number = int(response_text.split(" ")[0])

        logging.info(f'Check if {number} is in {interval}')
        return number in range(interval["min"], interval["max"] + 1)

    @staticmethod
    def number_in_rational_interval(response_text: str, interval: dict):
        """ Check if random number is within the specified rational interval"""
        logging.info("Get number")
        number = int(response_text.split(" ")[0])

        min_boundary, max_boundary = int(interval["min"]), int(interval["max"]) + 1
        logging.info(f'Check if {number} is in ({min_boundary}, {max_boundary})')
        return number in range(min_boundary, max_boundary)

    @staticmethod
    def is_random_number(response_text: str):
        """ Check if we receive a random number"""
        logging.info("Get number")
        number = response_text.split(" ")[0]

        logging.info(f'Check if {number} is a digit')
        return number.isdigit() or 'infinity' in number.lower() or 'e+' in number

    def build_url_with_interval(self, interval: dict) -> str:
        """ Build url for Random endpoint with specified interval"""
        random_url_with_interval = f'{self.endpoint_url}?min={interval["min"]}&max={interval["max"]}'
        logging.info(f'Random url with interval = {random_url_with_interval}')
        return random_url_with_interval
