# REST API for Alpha Vantage

The main goal of this project is to provide a BDD approach to verify how the Alpha Vantage API works

## 1. Environment setup

##### 1.1. Set Up a Python 3 development environment

##### 1.2. Using *virtualenv* is recommended (optional)

`pip install --upgrade virtualenv`

`python3 -m virtualenv --python python3 env`

`source ./env/bin/activate`

##### 1.3. Install the dependencies

`pip install -r requirements.txt`

## 2. Running the test suite

##### 2.1. Fire API tests

```
behave ./features --tags=-wip
```