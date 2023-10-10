import logging


class SubmitAPIEndpoint:
    def __init__(self):
        self.endpoint_url = 'http://numbersapi.com/submit'

    @staticmethod
    def is_empty_response_content(content: bytes) -> bool:
        """ Check if response content is empty """
        logging.info('Check if content contains only curly brackets')
        return len(content) == 2
