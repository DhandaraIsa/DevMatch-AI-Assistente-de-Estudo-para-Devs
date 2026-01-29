import os
import httpx
import asyncio

os.environ['GEMINI_API_KEY'] = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'

async def test_models():
    api_key = os.environ['GEMINI_API_KEY']
    models = ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-pro", "text-bison-001"]
    
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [{"role": "user", "parts": [{"text": "teste"}]}]
        }
        
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                r = await client.post(url, json=payload)
                print(f"\n{model}:")
                print(f"  Status: {r.status_code}")
                if r.status_code != 200:
                    print(f"  Response: {r.text[:200]}")
                else:
                    print(f"  ✅ Sucesso!")
        except Exception as e:
            print(f"\n{model}: ❌ {e}")

asyncio.run(test_models())
