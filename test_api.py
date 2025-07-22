import requests

url = "http://127.0.0.1:8000/ask/"
question = {
    "question": "What is my total sales?"
}
question = {
    "question": "Can you show sales by date?"
}
question= { 
    "question": "Show total units ordered per item"
}
question= {
  "question": "Which product had the highest clicks?"
}



response = requests.post(url, json=question)

print("Response:")
print(response.json())
