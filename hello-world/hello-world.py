import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr/local/spark/README.md')
print(txt.count())

python_lines = txt.filter(lambda line: 'python' in line.lower())
print("<<<Count number>>>-> {0}".format(python_lines.count()))
print("<<<The first line>>>-> {0}".format(python_lines.first()))
