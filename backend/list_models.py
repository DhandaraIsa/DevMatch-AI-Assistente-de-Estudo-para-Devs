import httpx
import json

api_key = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'
url = f"https://generativelanguage.googleapis.com/v1/models?key={api_key}"

try:
    response = httpx.get(url, timeout=10)
    print(f"Status: {response.status_code}\n")
    data = response.json()
    
    if "models" in data:
        print("Modelos disponíveis:")
        for model in data["models"]:
            print(f"  - {model.get('name', 'unknown')}")
    else:
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Erro: {e}")
-
