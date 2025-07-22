import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

SELECT ROUND(SUM(ad_sales) / SUM(ad_spend), 2) AS RoAS FROM ad_sales;

result = cursor.fetchone()

print(f"RoAS: {result[0]:.2f}")

conn.close()
