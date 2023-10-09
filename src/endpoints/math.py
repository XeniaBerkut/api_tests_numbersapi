from logging import Logger

from enums.endpoints import Endpoints


class Math:
    def __init__(self, logger: Logger, number: str):
        super().__init__()
        self.logger = logger
        self.number_url = Endpoints.BASE_URL.value + number + '/math'

    def is_correct_number_in_response(self, text: str, number: str) -> bool:
        self.logger.info(f'Check if {number} is in response text')
        if number in text:
            return True
        else:
            return False
