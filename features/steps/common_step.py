from datetime import date
from behave import then

from util import log_step_error


@then('response content should not be empty')
@log_step_error
def step_impl(context):
    assert context.response


@then('the rate should be equal or greater than the {benchmark} benchmark')
@log_step_error
def step_impl(context, benchmark):
    exchange_rate = list(context.response[0].values())[4]
    assert float(exchange_rate) >= float(benchmark)


@then('the value today should be equal or greater than the {benchmark} benchmark')
@log_step_error
def step_impl(context, benchmark):
    today = date.today()
    value = list(context.response[0][today.__str__()].values())[6]
    assert float(value) >= float(benchmark)
