
from operator import add

from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

lines = spark.read.text('file:////usr/local/spark/README.md').rdd.map(lambda r: r[0])
print("line number:", lines.count())
counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
    
spark.stop()