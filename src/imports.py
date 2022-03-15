import logging

LOGGING = {
    "format":'"timestamp": %(asctime)s, "type": "application_log", "schema":"json core", "application":"Flask demo app", "level":%(levelname)s, "message":%(message)s,',
    "datefmt": '%Y-%m-%dT%H:%M:%SZ',
    "level": logging.DEBUG,
    "encoding": 'utf-8'
}

class Service:
    def __init__(self, name, ready=True):
        self.name = name
        self.ready = ready
        logging.info(f"Start {self.name}.")

    def change_status(self):
        self.ready = not self.ready
        logging.info(f"{self.name} {'recovered' if self.ready else 'crashed'}.")