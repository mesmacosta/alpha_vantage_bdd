Feature: Digital Currency Value

  Scenario Outline: Digital Currency Value should be greater than the benchmark
    Given a Digital Currency <digital_currency> and Market <market>
     When Alpha Vantage is requested for the daily Digital Currency values
     Then response content should not be empty
      And the value today should be equal or greater than the <benchmark>

    Examples: Currencies and Benchmark
    | digital_currency  | market |benchmark |
    | BTC               | USD    |   9500   |
    | ETH               | USD    |   160    |