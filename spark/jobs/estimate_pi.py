from pyspark import SparkConf, SparkContext
from random import random

# Configure Spark to connect to the local cluster
conf = SparkConf().setAppName("PiEstimation").setMaster("spark://localhost:7077")
sc = SparkContext(conf=conf)

NUM_SAMPLES = 1000000

def inside(_):
    x, y = random(), random()
    return x*x + y*y < 1

# Parallelize the computation
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()

pi_estimate = 4.0 * count / NUM_SAMPLES
print(f"Pi is roughly {pi_estimate}")

sc.stop()
