#!/usr/bin/env python3
"""
Teste detalhado do Gemini API
"""

import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyDEAIbwOzB-Zt1l6ES7WdmLv9DT_f0bfuI'

try:
    import google.generativeai as genai
    
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    
    # Teste direto
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content("Diga uma piada!")
    
    print(f"✅ SUCESSO!\n\nResposta:\n{response.text}")
    
except Exception as e:
    print(f"❌ ERRO: {e}")
-
