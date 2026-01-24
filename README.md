# DevMatch AI 🤖📚  
### Assistente de Estudo para Desenvolvedores

O **DevMatch AI** é uma aplicação full stack que utiliza **Inteligência Artificial** para ajudar desenvolvedores a estudarem de forma mais eficiente, personalizada e prática.

O usuário informa:
- O que está estudando (ex: Python, React, SQL)
- Seu nível (iniciante, médio ou avançado)

E o sistema:
✅ Gera um plano de estudo  
✅ Sugere exercícios  
✅ Cria perguntas de revisão  
✅ Explica erros de código  
✅ Guarda histórico de estudos  
✅ Possui sistema de login  
✅ Interface moderna em React  

---

## 🚀 Funcionalidades

- 🔐 Autenticação (login e cadastro)
- 🧠 Geração de plano de estudos com IA
- ❓ Geração de perguntas de treino
- 🐞 Explicação de erros de código
- 🕒 Histórico de interações
- 🌐 API REST em Python
- 💻 Frontend em React

---

## 🧩 Tecnologias Utilizadas

### Backend
- Python  
- FastAPI  
- SQLAlchemy  
- SQLite  
- JWT (autenticação)  
- API de IA (Gemini/OpenAI)

### Frontend
- React  
- JavaScript  
- Axios  
- Vite  

---

## 📁 Estrutura do Projeto

devmatch-ai/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── database.py
│ │ ├── schemas.py
│ │ ├── auth.py
│ │ └── ai.py
│ └── requirements.txt
└── frontend/
├── src/
│ ├── pages/
│ ├── components/
│ ├── api.js
│ └── App.jsx
└── package.json

yaml
Copiar código

---

## ⚙️ Como rodar o projeto

### 🔹 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Configure sua variável de ambiente da API de IA:

bash
Copiar código
setx GEMINI_API_KEY "SUA_CHAVE"
🔹 Frontend
bash
Copiar código
cd frontend
npm install
npm run dev
🌐 Endpoints principais
Método	Rota	Descrição
POST	/auth/register	Cadastro
POST	/auth/login	Login
POST	/ai/plan	Gera plano de estudo
POST	/ai/questions	Gera perguntas
POST	/ai/explain	Explica erros
GET	/history	Histórico

🧠 O que este projeto demonstra
Consumo de API com IA

Backend em Python

Frontend em React

Autenticação JWT

Organização em camadas

Banco de dados

Arquitetura full stack

🚀 Melhorias futuras
Sistema de progresso do aluno

Favoritar planos

Dark mode

Deploy (Render/Vercel)

Notificações

Gamificação

👩‍💻 Autora
Dhandara Osserio
Desenvolvedora Full Stack Júnior
HTML | CSS | JavaScript | Python | C# | .NET | SQL
- Variáveis sensíveis devem estar em `.env`
# DevMatch-AI-Assistente-de-Estudo-para-Devs
# DevMatch-AI-Assistente-de-Estudo-para-Devs
# DevMatch-AI-Assistente-de-Estudo-para-Devs
