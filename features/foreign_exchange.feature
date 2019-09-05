Feature: Foreign Exchange

  Scenario Outline: Exchange rate should be greater than the benchmark
    Given a Currency Pair <source_currency> to <target_currency>
     When Alpha Vantage is requested for the Currency Pair Exchange rate
     Then response content should not be empty
      And the rate should be equal or greater than the <benchmark> benchmark

    Examples: Currencies and Benchmark
    | source_currency   | target_currency   | benchmark |
    | EUR               | USD               |    1.07   |
    | USD               | JPY               |    1.07   |
    | GBP               | USD               |    1.07   |
