import requests
import os
import re

def question_to_sql(question):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "API key not set."

    # ✅ Your updated prompt
    prompt = f"""
You are an expert SQL assistant. Convert the following natural language question into an SQL query for a SQLite database with these tables:

1. ad_sales (date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. total_sales (date, item_id, total_sales, total_units_ordered)
3. eligibility (item_id, is_eligible)

Use the exact column names shown above.

Assume RoAS = SUM(ad_sales) / SUM(ad_spend). Only use the ad_sales table to calculate it.

Only return the SQL code. Do not explain anything.

Question: "{question}"
"""

    # Gemini API URL
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        sql_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        
        # ✅ Remove ```sql or ``` from the response
        sql_code = re.sub(r"```(?:sql)?\n?", "", sql_text, flags=re.IGNORECASE).strip()
        sql_code = sql_code.replace("```", "").strip()

        return sql_code

    except Exception as e:
        return f"Error: {str(e)}\nFull response: {response.text}"
