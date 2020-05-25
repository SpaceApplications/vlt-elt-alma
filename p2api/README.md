# Phase 2 API tests

## Prerequisites

### Installing dependencies

Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Running the tests

Use the following command to run the tests:

```
pytest
```

Example output:

```
========================================= test session starts ==========================================
platform linux -- Python 3.7.4, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: p2api_test
collected 8 items

test_delete_finding_chart.py ........                                                            [100%]

========================================== 8 passed in 7.70s ===========================================
```

Use the option `--html=<report name>.html` to generate a HTML report for the test results:

```
pytest --html=results.html
```
