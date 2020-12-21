# Examples for testing pyspark without conftest

## Directory Structure

Under without_conftest/

| Path | Description |
| --- | --- |
|./| test root = without_conftest|
|./src/app| main application code|  
|./src/job| spark job code, require spark session|
|./src/service| task, no require spark session|
|./tests/| all test code |


## Run test

under "without_conftest"

``` shell 
python -m pytest tests/<testcases>.py
# Show detail
python -m pytest -s tests/<testcases>.py
```

## Test cases
* test_utils

    test pyspark basic functions

* test_pyspark_basic_etl

    test pyspark basic etl functions