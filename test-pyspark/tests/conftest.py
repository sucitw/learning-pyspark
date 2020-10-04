import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope='session')
def spark_session():
    """ fixture for creating a spark context
    Args:
        request: pytest.FixtureRequest object
    """
    spark_session = SparkSession.builder \
        .master("local[*]") \
        .appName("pyspark_test") \
        .getOrCreate()
        
    request.addfinalizer(lambda: spark_session.sparkContext.stop())
    
    return spark_session