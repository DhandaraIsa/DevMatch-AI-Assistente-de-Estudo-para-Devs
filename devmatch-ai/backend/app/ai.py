import os
import httpx

GEMINI_MODEL = "gemini-1.5-flash"

def _api_key() -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("GEMINI_API_KEY não configurada no ambiente.")
    return key

async def gemini_generate(prompt: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={_api_key()}"
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}]
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

def prompt_plan(topic: str, level: str) -> str:
    return f"""
Você é um mentor de programação. Crie um PLANO DE ESTUDO em 7 dias para o tema: {topic}.
Nível do aluno: {level}.

Regras:
- Seja direto, organizado e prático.
- Para cada dia, inclua: objetivos, conteúdos, 1 exercício e 1 mini desafio.
- Inclua links genéricos (ex: "documentação oficial") sem URLs.
- Responda em Markdown.
"""

def prompt_questions(topic: str, level: str) -> str:
    return f"""
Crie 10 perguntas de revisão sobre {topic} para nível {level}.
Regras:
- Misture: conceitos, prática e pegadinhas comuns.
- Forneça gabarito no final.
- Responda em Markdown.
"""

def prompt_explain(topic: str, level: str, error_text: str) -> str:
    return f"""
Explique e ajude a corrigir o erro abaixo, no contexto de {topic} (nível {level}).

Erro/código:
{error_text}

Regras:
- Explique como se fosse para uma pessoa júnior.
- Diga: causa provável, como confirmar, e como corrigir.
- Inclua um exemplo corrigido se possível.
- Responda em Markdown.
"""
