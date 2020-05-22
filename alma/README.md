# Selenium tests

## Prerequisites

### Installing selenium and pytest

Run the following command to install selenium and pytest

```
pip install -r requirements.txt
```

### Installing the web driver

Install the web driver for the browser that you wish to use.

See https://selenium-python.readthedocs.io/installation.html#drivers

## Running the tests

Use the following command to run the tests:

```
pytest --driver=chrome --ous_id='uid://A002/X639a2a/X2a'
```

Supported drivers are `chrome`, `firefox`, `edge`, `safari`.

Example output:

```
========================================= test session starts ==========================================
platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: /home/cmi/selenium_almascience
collected 1 item

test_almascience.py .                                                                            [100%]

========================================== 1 passed in 10.75s ==========================================
```
