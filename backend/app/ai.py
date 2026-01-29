import os
from dotenv import load_dotenv

load_dotenv()


def _api_key() -> str:
    """Get Gemini API key from environment"""
    key = os.getenv("GEMINI_API_KEY", "").strip()
    return key if key else None


async def gemini_generate(prompt: str) -> str:
    """Generate response from Google Gemini API using the official SDK"""
    
    api_key = _api_key()
    use_mock = os.getenv("USE_MOCK_AI", "false").lower() == "true"
    
    if not api_key or use_mock:
        return generate_mock_response(prompt)
    
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=api_key)
        
        # Modelos disponíveis em janeiro 2025
        # gemini-1.5-* foram descontinuados, usando versões 2.0 e 2.5
        models_to_try = [
            "gemini-2.0-flash",        # Recomendado - muito rápido e capaz
            "gemini-pro-latest",       # Alternativa estável
            "gemini-flash-latest",     # Outro alias para flash
        ]
        
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt, stream=False)
                if response and response.text:
                    return response.text
            except Exception as model_error:
                # Continua para o próximo modelo
                continue
        
        # Se nenhum modelo funcionou, retorna resposta mock
        return generate_mock_response(prompt)
        
    except ImportError:
        # google-generativeai não instalado
        return generate_mock_response(prompt)
    except Exception as e:
        # Qualquer outro erro, retorna resposta mock
        return generate_mock_response(prompt)


def generate_mock_response(prompt: str) -> str:
    """Generate a mock AI response for testing/offline mode"""
    
    if "plano" in prompt.lower() or "study" in prompt.lower():
        return """## Plano de Estudo Personalizado

### Dia 1: Fundamentos
- Objetivo: Entender conceitos básicos
- Exercício: Implemente um exemplo simples
- Desafio: Adapte o código para outro caso

### Dia 2-3: Prática Intermediária
- Objetivo: Dominar padrões comuns
- Exercício: Resolva 5 problemas
- Desafio: Crie um mini-projeto

### Dia 4-7: Aprofundamento
- Objetivo: Consolidar conhecimento
- Exercício: Projetos maiores
- Desafio: Contribua em projeto real"""
    
    elif "question" in prompt.lower() or "pergunta" in prompt.lower():
        return """## Questões de Revisão

1. Qual é a diferença entre teoria e prática?
2. Como você testaria seu entendimento?
3. Qual é a melhor estratégia para aprender?

**Gabarito:**
1. Teoria fornece base conceitual; Prática consolida entendimento
2. Com exercícios, testes e ensinando outros
3. Estudar → Praticar → Revisar → Ensinar outros"""
    
    elif "explain" in prompt.lower() or "explica" in prompt.lower():
        return """## Explicação Detalhada

Este conceito é importante porque:

1. Fornece base para tópicos mais avançados
2. É amplamente usado em aplicações reais
3. Facilita compreensão de padrões de design

**Exemplos práticos:**
- Aplicação simples do conceito
- Caso de uso em projeto real
- Variação avançada

Estude mais este tópico nos recursos oficiais."""
    
    return """## Resposta do Modo Offline

O DevMatch AI está em modo offline. Para respostas personalizadas da IA:

1. Verifique sua conexão com a internet
2. Configure uma chave válida da API do Google Gemini
3. Ou use o modo mock para testes

**Recomendações para estudo:**
- Revise os conceitos principais
- Faça exercícios práticos
- Procure ajuda nos recursos oficiais"""


def prompt_plan(topic: str, level: str) -> str:
    """Generate a prompt for creating a study plan"""
    return f"""Você é um mentor de programação experiente. Crie um PLANO DE ESTUDO em 7 dias para: {topic}.
Nível do aluno: {level} (iniciante/intermediário/avançado).

Estruture o plano assim:
- Para cada dia: objetivo, conteúdos principais, 1 exercício prático e 1 mini-desafio
- Use exemplos práticos e reais
- Seja motivador e encorajador

Responda em Markdown bem formatado."""


def prompt_questions(topic: str, level: str) -> str:
    """Generate a prompt for creating review questions"""
    return f"""Crie 10 perguntas de revisão sobre {topic} (nível {level}).

Instruções:
- Misture perguntas sobre conceitos e prática
- Inclua pegadinhas comuns
- Forneça gabarito detalhado no final
- Inclua dicas para responder corretamente

Responda em Markdown."""


def prompt_explain(topic: str, level: str, error_text: str) -> str:
    """Generate a prompt for explaining errors or concepts"""
    return f"""Você é um mentor que ajuda alunos a entenderem erros e conceitos.

Tema: {topic}
Nível do aluno: {level}

Erro ou dúvida do aluno:
```
{error_text}
```

Explique:
1. O que significa este erro ou conceito
2. Porque é importante entender isto
3. Como corrigir ou aplicar corretamente
4. Exemplos práticos

Seja claro, conciso e encorajador. Responda em Markdown."""

