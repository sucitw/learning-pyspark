
import pyspark.sql.functions as F
from pyspark.sql.types import *


def test_cast_arraytype(spark):
    data = [
        ("camilo", "colombia"),
        ("maria", "colombia")
    ]
    df = spark.createDataFrame(data, StructType([
        StructField("first_name", StringType(), True),
        StructField("country", StringType(), True, {'model_version': 3})
    ]))

    df.show()
    df.printSchema()

    df.write.mode('overwrite').parquet('tmp/people_with_metadata')