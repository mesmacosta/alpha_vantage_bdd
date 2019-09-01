import logging
import os


def before_all(context):
    __setup_logging()
    context.vars = {}
    # Change for your api key
    context.apy_key = 'YOUR-kEY'


def __setup_logging():
    logging.basicConfig(level=logging.ERROR)
