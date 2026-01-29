import sys
import os
import asyncio
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend"))

# Force set a new API key
os.environ['GEMINI_API_KEY'] = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend\app\.env"))

from app.ai import gemini_generate, prompt_plan

async def test_api():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        print("🔄 Testando API do Gemini...")
        print(f"  API Key configurada: {api_key[:25]}...")
        
        prompt = prompt_plan("Python Básico", "beginner")
        print(f"\n📝 Prompt enviado para o Gemini...")
        
        response = await gemini_generate(prompt)
        print(f"\n✅ Resposta recebida!")
        print(f"\n📄 Resposta (primeiros 300 caracteres):")
        print(response[:300] + "...")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_api())
