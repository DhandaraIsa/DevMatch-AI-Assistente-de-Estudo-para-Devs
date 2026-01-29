import google.generativeai as genai

api_key = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'
genai.configure(api_key=api_key)

# Listar modelos disponíveis
print("Modelos disponíveis para generateContent:")
for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"  ✅ {model.name}")

print("\n\nTentando chamar Gemini API...")
try:
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content("Olá, como você está?")
    print(f"✅ Sucesso!\nResposta: {response.text[:100]}")
except Exception as e:
    print(f"❌ Erro: {e}")
