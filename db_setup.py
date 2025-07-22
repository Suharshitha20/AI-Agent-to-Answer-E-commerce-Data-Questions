import pandas as pd
import sqlite3
import os

def load_data_to_db():
    conn = sqlite3.connect('ecommerce.db')
    
    files = {
        "ad_sales": "data/Product-Level Ad Sales and Metrics.csv",
        "total_sales": "data/Product-Level Total Sales and Metrics.csv",
        "eligibility": "data/Product-Level Eligibility Table.csv"
    }

    for table, filepath in files.items():
        df = pd.read_csv(filepath)
        df.to_sql(table, conn, if_exists="replace", index=False)
        print(f"Loaded {table}")

    conn.close()

if __name__ == "__main__":
    load_data_to_db()
