from behave import when

from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.cryptocurrencies import CryptoCurrencies

from util import log_step_error


@when('Alpha Vantage is requested for the Currency Pair Exchange rate')
@log_step_error
def step_impl(context):
    currency_pair = context.vars['currency_pair']

    foreign_exchange = ForeignExchange(key=context.apy_key)
    response = foreign_exchange.get_currency_exchange_rate(
        from_currency=currency_pair['source'],
        to_currency=currency_pair['target'])

    context.response = response


@when('Alpha Vantage is requested for the daily Digital Currency values')
@log_step_error
def step_impl(context):
    digital_currency = context.vars['digital_currency']

    crypto_currencies = CryptoCurrencies(key=context.apy_key)
    response = crypto_currencies.get_digital_currency_weekly(
                                      symbol=digital_currency['currency'],
                                      market=digital_currency['market'])

    context.response = response

