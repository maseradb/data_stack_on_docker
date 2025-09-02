docker compose up -d --build

# Data Stack on Docker

A robust, production-ready data processing environment using Docker Compose. This stack integrates Apache Airflow, Apache Spark, PostgreSQL, and JupyterHub, enabling scalable ETL, analytics, and collaborative data science workflows.

## Features

- **Apache Airflow**: Orchestrate complex data pipelines with a modern scheduler and UI.
- **Apache Spark**: Distributed data processing and analytics, with scalable worker configuration.
- **PostgreSQL**: Reliable, production-grade relational database for metadata and analytics.
- **JupyterHub**: Multi-user Jupyter Notebooks for collaborative data exploration and development.
- **NativeAuthenticator**: Simple, secure user management for JupyterHub.
- **Unified Docker Network**: All services communicate over a dedicated Docker bridge network.

---

## Architecture

```
[ JupyterHub ] <---> [ Spark Master & Workers ]
    |                        ^
    v                        |
[ PostgreSQL ] <----------> [ Airflow ]
```

- All services are containerized and connected via the `data-processing` Docker network.
- Data, logs, and configuration are persisted via Docker volumes.

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/maseradb/data_stack_on_docker.git
cd data_stack_on_docker
```

### 2. Create the Docker Network

```bash
docker network create --driver bridge data-processing
# Optional: Specify subnet to avoid conflicts
# docker network create --subnet=172.30.0.0/16 --driver bridge data-processing
```

### 3. Configure Environment Variables

Edit the `.env` files in each service directory (`postgres`, `airflow`, `jupyterhub`) with your credentials and settings.

### 4. Start PostgreSQL

```bash
cd postgres
docker compose up -d
```

### 5. Start Airflow

```bash
cd ../airflow
mkdir -p ./dags ./logs ./plugins ./config ./wallet
docker compose up airflow-init
docker compose up -d
```

### 6. Start Spark Cluster

```bash
cd ../spark
mkdir -p ./data ./jobs ./logs ./wallet ./work
docker compose up -d --scale worker=3
```

### 7. Start JupyterHub

```bash
cd ../jupyterhub
mkdir -p users jupyterhub_data
docker compose up -d --build
```

---

## Service URLs

- **Spark Master UI**: [http://localhost:9091](http://localhost:9091)
- **Spark History Server**: [http://localhost:18081](http://localhost:18081)
- **Airflow UI**: [http://localhost:8080](http://localhost:8080)
- **JupyterHub**: [http://localhost:8888](http://localhost:8888)

---

## Example: Running a PySpark Job

You can run distributed jobs using Spark from the `spark/jobs` directory. For example, to estimate Pi:

```bash
cd spark
spark-submit --master spark://localhost:7077 jobs/estimate_pi.py
```

Or use the provided Jupyter notebook for interactive Spark sessions.

---

## Tips & Troubleshooting

- Ensure all `.env` files are properly configured before starting services.
- If you encounter file permission issues (especially with JupyterHub secrets), ensure the correct user and permissions are set, or run the stack from a WSL-native path.
- Scale Spark workers as needed with `docker compose up -d --scale worker=N`.

---

## License

MIT License

---

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

---
