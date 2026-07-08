# 🚀 End-to-End AWS Data Engineering Pipeline

An end-to-end AWS Data Engineering project that automatically fetches datasets from a GitHub repository using the GitHub REST API, processes the data through a Medallion Architecture (Bronze, Silver, Gold), and makes it available for analytics using Athena and Power BI.

---

# 📌 Project Overview

This project demonstrates a production-style data engineering pipeline using AWS services, Apache Airflow, Apache Spark, AWS Glue, and GitHub API.

The pipeline automates:

- Fetching datasets from GitHub using GitHub REST API
- Loading raw data into Amazon S3 (Bronze Layer)
- Data transformation using Apache Spark
- Data catalog creation using AWS Glue Crawler
- Querying data with Amazon Athena
- Analytics using Power BI
- Workflow orchestration with Apache Airflow

---

# 🏗️ Architecture

```
GitHub Repository
        │
GitHub REST API
        │
Apache Airflow
        │
Amazon S3 (Bronze)
        │
Apache Spark
        │
Amazon S3 (Silver)
        │
Amazon S3 (Gold)
        │
Glue Crawler
        │
Glue Data Catalog
        │
Amazon Athena
        │
Power BI / Users
```

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Workflow Orchestration | Apache Airflow |
| Data Storage | Amazon S3 |
| Data Processing | Apache Spark (PySpark) |
| Metadata Catalog | AWS Glue Crawler |
| Query Engine | Amazon Athena |
| Visualization | Power BI |
| Version Control | GitHub |
| Data Source | GitHub REST API |
| Cloud Platform | AWS |
| Security | AWS IAM |

---

# 📂 Project Structure

```
Airflow_AWS_DataPipeline
│
├── airflow/
│   ├── dags/
│   └── plugins/
│
├── spark/
│
├── scripts/
│
├── datasets/
│
├── notebooks/
│
├── images/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Data Source

Datasets are stored in a GitHub repository and are automatically downloaded using the GitHub REST API.

Example workflow:

1. Airflow triggers the pipeline.
2. Python connects to the GitHub API.
3. Dataset files are downloaded.
4. Files are uploaded to Amazon S3 Bronze Layer.

---

# 🔄 Pipeline Workflow

### Step 1

Apache Airflow triggers the DAG.

↓

### Step 2

Python fetches datasets from GitHub using the GitHub REST API.

↓

### Step 3

Raw CSV files are stored in Amazon S3 Bronze Layer.

↓

### Step 4

Apache Spark cleans and transforms the data.

↓

### Step 5

Processed data is written to the Silver Layer.

↓

### Step 6

Business-ready datasets are written to the Gold Layer.

↓

### Step 7

AWS Glue Crawler scans the Gold Layer and updates the Glue Data Catalog.

↓

### Step 8

Amazon Athena queries the cataloged datasets.

↓

### Step 9

Power BI connects to Athena for reporting and dashboards.

---

# 🥉 Bronze Layer

- Raw datasets downloaded from GitHub API
- Stored without modifications
- Source of truth

---

# 🥈 Silver Layer

- Cleaned datasets
- Standardized schema
- Removed duplicates
- Handled missing values

---

# 🥇 Gold Layer

- Analytics-ready datasets
- Aggregated business metrics
- Optimized for reporting

---

# 🔐 Security

AWS IAM is used to manage permissions for:

- Amazon S3
- AWS Glue
- Athena
- Airflow

---

# 📈 Data Flow

```
GitHub Repository
        │
GitHub REST API
        │
Apache Airflow
        │
Amazon S3 Bronze
        │
Apache Spark
        │
Amazon S3 Silver
        │
Amazon S3 Gold
        │
Glue Crawler
        │
Glue Data Catalog
        │
Amazon Athena
        │
Power BI
```

---

# 🎯 Key Features

- Automated data ingestion from GitHub
- Apache Airflow orchestration
- Medallion Architecture
- Apache Spark transformations
- AWS Glue Data Catalog
- Amazon Athena analytics
- Power BI dashboards
- IAM-based security

---

# 📚 Skills Demonstrated

- Python
- Apache Airflow
- GitHub REST API
- AWS S3
- Apache Spark (PySpark)
- AWS Glue
- Amazon Athena
- Power BI
- Data Lake Architecture
- ETL Pipeline Development

---

# 👩‍💻 Author

**Monikashwari**

Aspiring Data Engineer

### Skills

- Python
- SQL
- PySpark
- Apache Airflow
- AWS
- Athena
- AWS Glue
- Amazon S3
- Power BI

---

⭐ If you found this project useful, consider giving it a Star!
