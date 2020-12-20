# Examples for testing pyspark

## Directory Structure

Under learn_test_pyspark/

| Path | Description |
| --- | --- |
|./| test root = learn_test_pyspark|
|./examples/test_project/src/app| main application code|  
|./examples/test_project/src/job| spark job code, require spark session|
|./examples/test_project/src/service| task, no require spark session|
|./examples/test_project/tests/| all test code |
|./examples/without_conftest/| examples test code without conftest|


## Run test

under the "test_project" or "without_conftest"

``` shell 
python -m pytest tests/<testcases>.py
```