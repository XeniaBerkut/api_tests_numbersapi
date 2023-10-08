from logging import Logger

from enums.endpoints import Endpoints


class Random:
    def __init__(self, logger: Logger):
        super().__init__()
        self.logger = logger

    def number_in_interval(self, response_text: str, interval: dict):
        number = int(response_text.split(" ")[0])
        self.logger.info(f'Check if {number} in {interval}')
        if number in range(interval["min"], interval["max"]):
            return True
        else:
            return False

    def set_url_with_interval(self, interval: dict) -> str:
        endpoint_interval = f'?min={interval["min"]}&max={interval["max"]}'
        random_url = str(Endpoints.RANDOM.value) + endpoint_interval
        self.logger.info(f'Random url with interval = {random_url}')
        return random_url
