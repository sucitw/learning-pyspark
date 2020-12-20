"""
Test utilities to creat the spark context
"""
import os
import sys
import unittest
from operator import add
from pyspark import SparkConf
from pyspark.sql import SparkSession


class SparkTestClass(unittest.TestCase):

    def setUp(self):
        """Create a single node Spark application."""
        self._old_sys_path = list(sys.path)
        conf = SparkConf()
        conf.set("spark.executor.memory", "1g")
        conf.set("spark.cores.max", "1")
        conf.set("spark.app.name", self.__class__.__name__)
        SparkSession._instantiatedContext = None
        self.spark = SparkSession.builder.config(conf=conf).getOrCreate()
        self.sc = self.spark.sparkContext
        

    def tearDown(self):
        """Stop the SparkContext."""
        self.sc.stop()
        self.spark.stop()
        sys.path = self._old_sys_path



class SimpleWordCountTest(SparkTestClass):
    def test_basic(self):
        test_rdd = self.sc.parallelize(['cat dog mouse','cat cat dog'], 2)
        results = test_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(add).collect()
        expected_results = [('cat', 3), ('dog', 2), ('mouse', 1)]
        self.assertEqual(set(results), set(expected_results))