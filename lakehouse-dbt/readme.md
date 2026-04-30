# Lakehouse Project

Welcome to the **Lakehouse Project** repository! This project leverages a powerful stack of modern data tools to create an efficient and scalable Lakehouse architecture. By integrating **DBT**, **Dremio**, **MinIO**, **Airflow** with **Astronomer Cosmos**, and **Apache Iceberg**, this project provides a comprehensive framework for seamless data engineering, analytics, and governance.

## Project Overview

The Lakehouse Project is designed to bridge the best aspects of data lakes and data warehouses, delivering a robust environment that supports large-scale data ingestion, transformation, storage, and querying. Here’s a quick look at each tool’s role within our architecture:

- **DBT (Data Build Tool)**: Our data transformations and modeling are powered by DBT, providing a version-controlled and SQL-centric approach to transforming raw data into valuable insights. With DBT, transformations are written as modular, reusable code that integrates well into our CI/CD workflows.

- **Dremio**: Serving as our high-performance query engine, Dremio offers fast access to data across various storage formats, including Iceberg tables. By using Dremio, users can interact with data directly from the lakehouse with SQL, reducing the need for data movement.

- **MinIO**: Acting as the backbone of our storage layer, MinIO is a high-performance, S3-compatible object storage service. It enables scalable data storage, with data kept in its raw format, making it ideal for storing both structured and unstructured data.

- **Apache Iceberg**: Iceberg provides an optimized table format designed for high-volume analytics workloads, with support for schema evolution, partitioning, and versioning. It ensures consistent and efficient query performance within our lakehouse.

- **Airflow with Astronomer Cosmos**: Orchestrating data pipelines is streamlined with Apache Airflow, enhanced by the Astronomer Cosmos tool to simplify the integration of DBT models into the orchestration layer. This combination allows for seamless data workflows and job scheduling, with Astronomer Cosmos automating the creation of DAGs for DBT models.

## Key Features

- **Unified Data Access**: Query data across structured and unstructured sources seamlessly with Dremio and Iceberg, minimizing data movement.
- **Scalable Storage**: Store massive datasets efficiently on MinIO, leveraging S3-compatible object storage.
- **Transformative Analytics**: With DBT, transform raw data into business-ready analytics models, supporting data consistency across teams.
- **Automated Workflows**: Using Airflow and Astronomer Cosmos, we automate pipeline orchestration for scalable, reliable data processing.

## Getting Started

To get started with this project, follow the installation and configuration steps in the setup guide [link to setup guide]. Ensure that you have Docker and Kubernetes (or similar orchestration tools) to manage the necessary containers. Refer to the individual documentation of each service for additional setup details.

---

With this stack, the Lakehouse Project enables an end-to-end solution for data engineering and analytics, setting up your team for success in a modern data environment. Explore the documentation, clone the repository, and start building your Lakehouse today!

## Install packages
```bash
#listar versões de dbt instaladas
pip list | grep dbt

#remover todas as bibliotecas que começam com dbt
pip uninstall --break-system-packages -y $(pip list --format=freeze | grep '^dbt-' | cut -d= -f1)

#intalar na sequencia:
dbt-core==1.8.0
dbt-dremio==1.8.1

#verificar instalação 
pip list | grep dbt

```