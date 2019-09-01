import logging

from .module_logger_factory import ModuleLoggerFactory

logger = ModuleLoggerFactory.make_file_logger(
    module_name='alpha_vantage_bdd.step_error_logger',
    file_name='log/exec_errors.log',
    log_format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    log_level=logging.ERROR
)


def log_step_error(func):

    def function_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            context = args[0]
            feature = context._stack[1]['feature'].name
            scenario = context._stack[0]['scenario'].name

            logger.exception(f'\nFeature: {feature}\nScenario: {scenario}\nDetails: {e}\n')
            raise

    return function_wrapper
