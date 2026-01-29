🚀 DevMatch AI — Assistente de Estudo para Devs

DevMatch AI é uma plataforma web inteligente que utiliza Inteligência Artificial (Google Gemini) para auxiliar desenvolvedores em seus estudos, oferecendo planos personalizados, questões práticas e explicações de erros.

O projeto combina:

🧠 Backend em FastAPI

⚛️ Frontend em React + Vite

🗄️ Banco de dados MySQL

🤖 Integração com IA (Gemini API)

✨ Funcionalidades

✅ Cadastro e login de usuários (JWT)

📚 Geração de plano de estudos por tema e nível

📝 Geração de perguntas de prática

🧩 Explicação de erros e conceitos

🕓 Histórico de estudos salvo no banco

🔐 Autenticação segura

🌐 API documentada com Swagger

🧱 Arquitetura
DevMatch AI Assistente de Estudo para Devs/
├── .venv/                          # Ambiente virtual Python
├── backend/                         # Backend FastAPI
│   ├── app/
│   │   ├── main.py                # Aplicação FastAPI
│   │   ├── models.py              # Modelos SQLAlchemy
│   │   ├── schemas.py             # Schemas Pydantic
│   │   ├── database.py            # Configuração MySQL
│   │   ├── auth.py                # Autenticação JWT
│   │   ├── ai.py                  # Integração Gemini
│   │   ├── test_connection.py     # Teste do banco
│   │   ├── create_tables.py       # Criação das tabelas
│   │   └── create_mysql_setup.sql # Script SQL inicial
│   └── run_server.py              # Inicialização do servidor
└── frontend/                       # Frontend React + Vite
    ├── src/
    │   ├── main.jsx
    │   ├── app.jsx
    │   └── api.js
    ├── components/
    ├── pages/
    ├── index.html
    └── package.json

⚙️ Instalação e Execução
🔹 Backend

Ativar ambiente virtual:

cd "c:\Users\User\Documents\Dev\DevMatch AI Assistente de Estudo para Devs"
.\.venv\Scripts\activate


Instalar dependências:

cd backend\app
pip install -r requirements.txt


Executar servidor:

cd ..
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload


Acesse:

API: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

🔹 Frontend
cd frontend
npm install
npm run dev


Frontend em:
👉 http://localhost:5173

Build de produção:

npm run build

📡 Endpoints Principais
🔐 Autenticação

POST /auth/register — Registrar usuário

POST /auth/login — Login

🤖 IA

POST /ai/plan — Gerar plano de estudo

POST /ai/questions — Gerar questões

POST /ai/explain — Explicar erro ou conceito

📊 Histórico

GET /history — Buscar histórico do usuário

🔑 Variáveis de Ambiente

Arquivo .env em backend/app:

DATABASE_URL=mysql+pymysql://devuser:devpass@localhost:3306/devmatch
SECRET_KEY=sua-chave-secreta
GEMINI_API_KEY=sua-chave-gemini

🗄️ Banco de Dados

Banco: devmatch

Usuário: devuser

Porta: 3306

Scripts úteis:

test_connection.py — testar conexão

create_tables.py — criar tabelas

create_mysql_setup.sql — criar banco e usuário

🛠️ Tecnologias
Backend

FastAPI

SQLAlchemy

MySQL

Pydantic

Python-Jose

Passlib

Google Gemini API

PyMySQL

Frontend

React 18

Vite

Axios

CSS3

🔐 Segurança

Senhas com bcrypt

Autenticação via JWT

CORS configurado

Variáveis sensíveis armazenadas em .env

📌 Observações

✔️ Banco migrado de SQLite para MySQL

✔️ Estrutura separada entre backend e frontend

✔️ Projeto pronto para portfólio

✔️ Ideal para estágio ou vaga júnior

👩‍💻 Autora

Dhandara Osserio
Estudante de Análise e Desenvolvimento de Sistemas

