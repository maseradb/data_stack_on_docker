# Pyspark image creation

# SO Image base
FROM python:3.11-bullseye as spark-base

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      nano \
      unzip \
      rsync \
      openjdk-17-jre-headless \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Environment variables
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}
ENV PYSPARK_PYTHON=python3.11
ENV PYSPARK_DRIVER_PYTHON=python3.11

# Spark internal folders and variables
RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

# Download spark binaries
RUN curl https://archive.apache.org/dist/spark/spark-3.5.6/spark-3.5.6-bin-hadoop3.tgz -o spark-3.5.6-bin-hadoop3.tgz \
 && tar xvzf spark-3.5.6-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-3.5.6-bin-hadoop3.tgz

# Set up spark environment
FROM spark-base as pyspark

# Python dependencies
RUN pip install --upgrade pip
COPY requirements/requirements.txt .
RUN pip3 install -r requirements.txt

# Environment variables
ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

# Copy spark-defaults.conf
COPY conf/spark-defaults.conf "$SPARK_HOME/conf"

# Permissions
RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

# Copy the entrypoint script
COPY entrypoint.sh .

# Privileges on entrypoint
RUN chmod +x entrypoint.sh

# Entrypoint execution on start
ENTRYPOINT ["./entrypoint.sh"]
