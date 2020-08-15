
from pyspark import SparkConf, SparkContext

import collections as c

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("ml-100k/u.data")

lines.
