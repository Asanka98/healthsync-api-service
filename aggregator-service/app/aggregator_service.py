from fastapi import FastAPI, BackgroundTasks
from sqlalchemy import create_engine, text
import pandas as pd
import os
import sys

# Initialize FastAPI
app = FastAPI()

# Database configurations (from Kubernetes environment variables)
RDS_DB_URI = os.getenv("RDS_DB_URI")

# Check if RDS_DB_URI is provided
if not RDS_DB_URI:
    raise ValueError("Environment variable RDS_DB_URI is not set")

# RDS connection
rds_engine = create_engine(RDS_DB_URI)

# Aggregator function
def aggregate_data():
    try:
        # Fetch data from RDS
        with rds_engine.connect() as conn:
            query = """
                SELECT 
                    doctor_name, 
                    COUNT(*) AS appointment_count, 
                    MAX(appointment_time) AS last_update
                FROM 
                    appointments
                GROUP BY 
                    doctor_name;
            """
            data = pd.read_sql(text(query), conn)

        # Example: Store the aggregated data back into RDS (in a new table)
        with rds_engine.connect() as conn:
            data.to_sql("aggregated_data", conn, index=False, if_exists="replace")

        print("Data aggregation completed successfully")
    except Exception as e:
        print(f"Error occurred during aggregation: {e}")

# Root endpoint for health check
@app.get("/")
def read_root():
    return {"status": "Aggregator Service Running"}

# Endpoint to manually trigger aggregation
@app.post("/run-aggregation/")
def run_aggregation(background_tasks: BackgroundTasks):
    background_tasks.add_task(aggregate_data)
    return {"status": "Aggregation task started"}

# Main block for running the aggregation directly
if __name__ == "__main__":
    if "--run-aggregation" in sys.argv:
        print("Running aggregation task directly...")
        aggregate_data()
