# 🚀 End-to-End AWS Data Engineering Pipeline

An end-to-end AWS Data Engineering project that automates data ingestion from a GitHub repository using the GitHub REST API, processes data through a Medallion Architecture (Bronze, Silver, Gold), catalogs datasets with AWS Glue, and enables analytics using Amazon Athena and Power BI.

---

# 📌 Project Overview

This project demonstrates an end-to-end data engineering pipeline built using AWS services, Apache Airflow, Apache Spark (PySpark), and the GitHub REST API.

The pipeline automates:

- Fetching datasets from a GitHub repository using the GitHub REST API
- Loading raw data into Amazon S3 (Bronze Layer)
- Transforming and cleaning data using Apache Spark (PySpark)
- Organizing data into Bronze, Silver, and Gold layers
- Creating metadata using AWS Glue Crawler
- Querying processed data using Amazon Athena
- Visualizing insights using Power BI
- Orchestrating the entire workflow using Apache Airflow

---

# 🏗️ Architecture

![AWS Data Engineering Pipeline Architecture](./Screenshot%202026-07-08%20231726.png)

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Workflow Orchestration | Apache Airflow |
| Data Source | GitHub REST API |
| Data Storage | Amazon S3 |
| Data Processing | Apache Spark (PySpark) |
| Metadata Catalog | AWS Glue Crawler |
| Query Engine | Amazon Athena |
| Visualization | Power BI |
| Version Control | GitHub |
| Cloud Platform | AWS |
| Security | AWS IAM |
| Containerization | Docker, Docker Compose |

---

# 📂 Project Structure

```text
Airflow_AWS_DataPipeline/
│
├── config/                      # Airflow configuration
├── dags/                        # Airflow DAG definitions
├── logs/                        # Airflow execution logs
│
├── utils/
│   ├── Bronze_layer.py          # Bronze layer ingestion
│   ├── Silver_layer.py          # Silver layer transformation
│   ├── Gold_layer.py            # Gold layer processing
│   └── __init__.py
│
├── .env_example                 # Environment variables template
├── .gitignore
├── Dockerfile                   # Docker configuration
├── docker-compose.yaml          # Docker Compose configuration
├── Gold_Layer.ipynb             # Gold layer notebook
├── Screenshot 2026-07-08 231726.png
├── requirements.txt
└── README.md
```

---

# 📊 Data Source

The project retrieves datasets directly from a GitHub repository using the GitHub REST API.

The ingestion process performs the following steps:

1. Apache Airflow triggers the workflow.
2. Python authenticates with the GitHub REST API.
3. Dataset files are downloaded.
4. Raw files are uploaded to Amazon S3 Bronze Layer.

---

# 🔄 Pipeline Workflow

### Step 1

Apache Airflow schedules and triggers the pipeline.

↓

### Step 2

Python retrieves datasets from GitHub using the GitHub REST API.

↓

### Step 3

Raw CSV files are stored in the Amazon S3 Bronze Layer.

↓

### Step 4

Apache Spark (PySpark) cleans, validates, and transforms the raw data.

↓

### Step 5

Processed datasets are written into the Silver Layer.

↓

### Step 6

Business-ready datasets are stored in the Gold Layer.

↓

### Step 7

AWS Glue Crawler scans the Gold Layer and updates the AWS Glue Data Catalog.

↓

### Step 8

Amazon Athena queries the cataloged datasets.

↓

### Step 9

Power BI connects to Amazon Athena to create interactive dashboards and reports.

---

# 🥉 Bronze Layer

The Bronze Layer stores raw data exactly as received from the GitHub repository.

Features:

- Raw CSV datasets
- No transformations
- Source of truth
- Stored in Amazon S3

---

# 🥈 Silver Layer

The Silver Layer contains cleaned and standardized datasets.

Features:

- Missing values handled
- Duplicate records removed
- Standardized schema
- Data transformations using PySpark

---

# 🥇 Gold Layer

The Gold Layer stores analytics-ready datasets optimized for reporting.

Features:

- Aggregated business metrics
- Optimized analytical tables
- Reporting-ready datasets
- Used by Athena and Power BI

---

# 🔐 Security

AWS IAM is used to securely manage access to:

- Amazon S3
- AWS Glue
- Amazon Athena
- Apache Airflow

---

# ✨ Key Features

- Automated data ingestion from GitHub
- Apache Airflow workflow orchestration
- GitHub REST API integration
- Medallion Architecture (Bronze, Silver, Gold)
- Apache Spark (PySpark) data transformations
- AWS Glue Data Catalog integration
- Amazon Athena analytics
- Power BI reporting
- Docker-based deployment
- IAM-based security

---

# 📚 Skills Demonstrated

- Python
- SQL
- Apache Airflow
- Apache Spark (PySpark)
- GitHub REST API
- Amazon S3
- AWS Glue
- Amazon Athena
- Power BI
- Docker
- Docker Compose
- Data Lake Architecture
- ETL Pipeline Development

---
# ⚙️ Prerequisites

Before running the project, ensure you have:

- Python 3.10 or later
- Docker
- Docker Compose
- AWS Account
- AWS CLI configured
- GitHub Personal Access Token

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Monikashwari/Airflow_AWS_DataPipeline.git
```

## 2. Navigate to the project directory

```bash
cd Airflow_AWS_DataPipeline
```

## 3. Create a virtual environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install the required Python packages

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file using the `.env_example` template and update it with your:

- AWS Credentials
- GitHub Personal Access Token
- S3 Bucket Name
- Other required configuration values

## 6. Start Apache Airflow

```bash
docker-compose up
```

## 7. Access the Airflow Web UI

Open your browser and navigate to:

```text
http://localhost:8080
```

Default credentials:

```text
Username: airflow
Password: airflow
```

## 8. Trigger the DAG

Enable the DAG from the Airflow UI and trigger it to execute the complete data pipeline.

---

# 📈 Future Enhancements

- Incremental data loading
- Data quality validation
- Automated monitoring and alerting
- CI/CD pipeline integration
- Infrastructure as Code using Terraform
- Data lineage tracking

---

# 👩‍💻 Author

## Monikashwari

Aspiring Data Engineer

### Technical Skills

- Python
- SQL
- Apache Airflow
- PySpark
- AWS S3
- AWS Glue
- Amazon Athena
- Power BI
- Docker
