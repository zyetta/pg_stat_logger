# PostgreSQL Data Collector

## Setup Guide

### Setup Virtual Environment

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Requirements

2. Install dependencies listed in requirements.txt:
```
pip install -r requirements.txt
```

### Populate with Credentials

3. Populate your PostgreSQL credentials in the script:

```
hostname = '192.168.68.223'
database = 'postgres'
username = 'postgres'
password = 'postgres'
```

Ensure these credentials have appropriate permissions to access the PostgreSQL database.

# About the Code
This Python script connects to a PostgreSQL database and periodically fetches statistics from various views. It stores this data in CSV files for analysis or monitoring purposes.

### Code Explanation
- The script uses psycopg2 to connect to PostgreSQL and fetch statistics.
- It defines several SQL queries (queries dictionary) to fetch data from different PostgreSQL views.
- Data fetched from each query is stored in separate CSV files named after the corresponding view.
- The main function fetch_and_store_stats() fetches data, appends it to CSV files, and handles file creation and header writing if necessary.
- The script runs indefinitely in a loop (while True) fetching data every second (time.sleep(0.5)).

### Usage
> Baseline Data Collection: Before starting any experiments, run the script for about 5 minutes to establish a baseline of PostgreSQL performance metrics.

```
python main.py
```

### Note
Ensure the PostgreSQL server is accessible from the machine running this script.
This script runs indefinitely until interrupted by the user (Ctrl+C).