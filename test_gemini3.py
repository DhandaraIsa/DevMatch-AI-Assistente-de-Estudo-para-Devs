import asyncio
import os
import sys

# Adicionar backend ao path
sys.path.insert(0, "c:\\Users\\User\\Documents\\Dev\\DevMatch AI Assistente de Estudo para Devs\\backend")

# Configurar API Key
os.environ['GEMINI_API_KEY'] = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'
os.environ['USE_MOCK_AI'] = 'false'

from app.ai import gemini_generate, prompt_plan

async def test():
    print("🔄 Testando Gemini API com novo SDK...\n")
    
    # Teste 1: Simples
    prompt = prompt_plan("Python", "iniciante")
    print(f"📝 Enviando prompt:\n{prompt[:100]}...\n")
    
    try:
        response = await gemini_generate(prompt)
        print(f"✅ Resposta recebida:\n{response[:300]}...\n")
    except Exception as e:
        print(f"❌ Erro: {e}")

asyncio.run(test())
