# Data-Processing_v2

### Docker environment for data processing, with spark and airflow with postgresql as backgroud database
### Data discovery with jupyterhub, allowing multiple users/workspaces on jupyter notebook sessions


# Network

### First, create a network to avoid miscommunication between your containers
    docker network create --driver bridge data-processing

### Pay attention to avoid network conflicts
### If needed you can specify the network range, check routes before setting it
    docker network create --subnet=172.30.0.0/16 --driver bridge data-processing


# PostgreSQL
### Add your credentials to the .env file
    cd postgres
    docker compose up -d


# Airflow

### Create airflow containers
### Add your credentials to the .env file
    cd airflow 
    mkdir -p ./dags ./logs ./plugins ./config ./wallet
    docker compose up airflow-init 
    docker compose up -d

### Adjust airflow variables if needed:
    Adjust the user and password at the .env file


# Spark

### Here you can scale your cluster as needed, just edit the number at '--scale worker'
    cd spark
    mkdir -p ./data ./jobs ./logs ./ wallet
    docker compose up -d --scale worker=3


# Utility
### Spark Master
    http://localhost:9091

### History Server
    http://localhost:18081

### Airflow
    http://localhost:8080

# JupyterHub
    cd jupyerhub
    docker compose up -d