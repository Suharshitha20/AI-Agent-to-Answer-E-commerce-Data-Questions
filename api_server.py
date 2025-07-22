from fastapi import FastAPI
from pydantic import BaseModel
from llm_agent import question_to_sql
import sqlite3
from visualizer import plot_bar  # assumes you have visualizer.py for charting

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "AI Ecommerce Agent Running!"}

@app.post("/ask/")
async def ask_question(request: QuestionRequest):
    question = request.question.strip()

    sql = question_to_sql(question)

    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    try:
        # ✅ Special case for chart
        if "sales by date" in question.lower():
            chart_sql = "SELECT date, SUM(total_sales) FROM total_sales GROUP BY date"
            cursor.execute(chart_sql)
            result = cursor.fetchall()
            labels = [row[0] for row in result]
            values = [row[1] for row in result]
            chart_file = plot_bar(labels, values, title="Sales by Date")
            conn.close()
            return {
                "question": question,
                "sql_generated": chart_sql,
                "result": result,
                "chart_file": chart_file
            }

        # ✅ General case
        cursor.execute(sql)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

    except Exception as e:
        conn.close()
        return {
            "error": str(e),
            "sql_generated": sql
        }

    conn.close()
    return {
        "question": question,
        "sql_generated": sql,
        "columns": columns,
        "result": result
    }
