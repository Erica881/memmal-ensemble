from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_path = "maheshj01/sql-injection-classifier"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Function to classify a SQL query
def classify_query(query):
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    prediction = outputs.logits.argmax(-1).item()
    return "Vulnerable" if prediction == 1 else "Secure"

# Example usage
query = "SELECT * FROM users WHERE username = 'admin' OR '1'='1'"
result = classify_query(query)
print(f"The query is classified as: {result}")
