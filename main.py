import psycopg2
import csv
import time
from datetime import datetime

# Database connection details
hostname = '192.168.68.223'
database = 'postgres'
username = 'postgres'
password = 'postgres'

# Queries to fetch from PostgreSQL views
queries = {
    'pg_stat_database': "SELECT * FROM pg_stat_database;",
    'pg_stat_bgwriter': "SELECT * FROM pg_stat_bgwriter;",
    'pg_stat_user_tables': "SELECT * FROM pg_stat_user_tables;",
    'pg_stat_user_indexes': "SELECT * FROM pg_stat_user_indexes;",
    'pg_stat_activity': "SELECT * FROM pg_stat_activity;"
}

# Function to fetch and append PostgreSQL statistics to a single CSV file
def fetch_and_store_stats():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=hostname,
            database=database,
            user=username,
            password=password
        )

        cursor = connection.cursor()

        # Generate timestamp for file name
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Initialize a dictionary to hold file handlers for each query
        file_handlers = {}

        for query_name, query_string in queries.items():
            # Execute query
            cursor.execute(query_string)
            data = cursor.fetchall()

            # Determine filename and create file if not already opened
            if query_name not in file_handlers:
                filename = f"{query_name}_data.csv"
                file_handlers[query_name] = open(filename, mode='a', newline='')
                writer = csv.writer(file_handlers[query_name])

                # Write header only if file is newly created
                if file_handlers[query_name].tell() == 0:
                    writer.writerow([col.name for col in cursor.description])

            # Append data to CSV file
            writer = csv.writer(file_handlers[query_name])
            for row in data:
                writer.writerow(row)

            print(f"Data appended to {filename}")

        # Close all file handlers
        for handler in file_handlers.values():
            handler.close()

        # Close cursor and connection
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL:", error)

# Main loop to fetch and store data every second
if __name__ == "__main__":
    try:
        while True:
            fetch_and_store_stats()
            time.sleep(0.5)  # Sleep for 1 second

    except KeyboardInterrupt:
        print("Script interrupted by user.")
