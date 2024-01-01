import json
import logging
import datetime
import sys

class LoggerDefault:
    def __init__(self):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

    def register_info(self, message):
        log_entry = self._create_log_entry('INFO', message)
        logging.info(json.dumps(log_entry))

    def register_error(self, message, exception=None):
        log_entry = self._create_log_entry('ERROR', message, exception)
        logging.error(json.dumps(log_entry))

    def _create_log_entry(self, log_type, message, exception=None):
        log_entry = {
            'timestamp': self._get_timestamp(),
            'type': log_type,
            'message': message
        }

        if exception:
            log_entry['exception'] = str(exception)

        return log_entry

    def _get_timestamp(self):
        return datetime.datetime.utcnow().isoformat()
