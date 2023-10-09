from logging import Logger


class Submit:
    def __init__(self, logger: Logger):
        super().__init__()
        self.logger = logger

    def is_empty_response_content(self, content: str) -> bool:
        self.logger.info('Check if content contains only curly brackets')
        if len(content) == 2:
            return True
        else:
            return False
