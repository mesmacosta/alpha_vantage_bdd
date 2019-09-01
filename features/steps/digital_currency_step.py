from behave import given


@given('a Digital Currency {digital_currency} and Market {market}')
def step_impl(context, digital_currency, market):
    context.vars['digital_currency'] = {'currency': digital_currency, 'market': market}
