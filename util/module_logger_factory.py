import logging
import os


class ModuleLoggerFactory:

    @staticmethod
    def make_file_logger(module_name, file_name, log_format, log_level):
        module_logger = logging.getLogger(module_name)

        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        log_handler = logging.FileHandler(file_name, mode='w')
        log_handler.setFormatter(logging.Formatter(log_format))
        log_handler.setLevel(log_level)
        module_logger.addHandler(log_handler)

        return module_logger
