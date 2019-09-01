from behave import given


@given('a Currency Pair {source_currency} to {target_currency}')
def step_impl(context, source_currency, target_currency):
    context.vars['currency_pair'] = {'source': source_currency, 'target': target_currency}
