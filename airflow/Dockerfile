FROM apache/airflow:3.0.6-python3.11
USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  openjdk-17-jre-headless \
    vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen pt_BR.UTF-8

USER airflow

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

RUN pip install pyspark==3.5.6
RUN pip install apache-airflow-providers-apache-spark
RUN pip install oracledb