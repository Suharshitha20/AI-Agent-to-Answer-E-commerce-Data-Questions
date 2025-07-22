AI-Powered E-commerce SQL Assistant

This is a smart, AI-powered data query assistant that enables users to ask natural language questions and get precise SQL-based answers from an e-commerce dataset.

🔍 What It Does

This project uses FastAPI as a backend service, SQLite as the database, and Google Gemini (via API) to convert English questions into executable SQL. It also includes a bonus charting feature using matplotlib.

🛠️ Tech Stack

Python 3.x

FastAPI

SQLite

Google Gemini 1.5 Flash API

Matplotlib (for chart visualization)

Pydantic (request validation)

📁 Datasets Used

The following CSVs were used to create the database:

Product-Level Ad Sales and Metrics.csv

Product-Level Total Sales and Metrics.csv

Product-Level Eligibility Table.csv

These were loaded using db_setup.py into ecommerce.db.

📦 Features

✅ Natural language to SQL translation using LLM

✅ Works with multiple tables: ad_sales, total_sales, eligibility

✅ Query structured data and return answers in JSON

✅ Bonus: Generates bar chart when asking for "sales by date"

✅ Fully testable via Swagger UI or Python script

📌 Sample Questions to Ask
POST /ask/  with JSON:
{
  "question": "What is my total sales?"
}
Other examples:

"Calculate the RoAS"

"Which product had the highest clicks?"

"Can you show sales by date?"

🚀 How to Run It

Clone the repo and install requirements

Run db_setup.py to load the datasets

Start the API:
uvicorn api_server:app --reload
Open your browser to http://127.0.0.1:8000/docs

Use /ask/ endpoint and test your questions

📊 Chart Feature

When the question includes "sales by date", the app runs a custom SQL query and returns a chart.png file showing sales over time using matplotlib.

🔐 Setup Gemini API Key

In your terminal:
$env:GEMINI_API_KEY="AIzaSyA_lK0uLM1E-7xdbSl-i9DZXuIBO07fhYM"  (on Windows PowerShell)
File Structure
├── api_server.py
├── llm_agent.py
├── db_setup.py
├── test_api.py
├── visualizer.py
├── ecommerce.db
✅ Status

100% complete ✅Tested and submission-ready 🎯Includes both core functionality and optional bonus!
