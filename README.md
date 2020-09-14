# learning-pyspark
Notes and materials to learn Pyspark


# Environment setup

Single node and cluster (multiple node)

### Quick way to build a pyspark env 

Please replace **/Users/shuhsi/github** with your own folder.
```
docker run -it --rm -p 8888:8888 -v /Users/shuhsi/github:/home/jovyan/work jupyter/pyspark-notebook
```

- [Running PySpark on Jupyter Notebook with Docker](https://medium.com/@suci/running-pyspark-on-jupyter-notebook-with-docker-602b18ac4494)
- [Apache Spark Cluster on Docker (ft. a JupyterLab Interface)](https://towardsdatascience.com/apache-spark-cluster-on-docker-ft-a-juyterlab-interface-418383c95445)