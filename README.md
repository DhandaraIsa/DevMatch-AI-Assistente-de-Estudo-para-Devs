# DevMatch AI - Assistente de Estudo para Devs

Plataforma web inteligente que combina um backend FastAPI com um frontend React/Vite para criar um assistente de estudo alimentado por IA (Gemini).

## 📁 Estrutura do Projeto

```
DevMatch AI Assistente de Estudo para Devs/
├── .venv/                          # Ambiente virtual Python
├── backend/                         # Backend FastAPI (movido de devmatch-ai/)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                # Aplicação FastAPI principal
│   │   ├── models.py              # Modelos SQLAlchemy (User, StudyItem)
│   │   ├── schemas.py             # Schemas Pydantic (validação de dados)
│   │   ├── database.py            # Configuração do banco de dados MySQL
│   │   ├── auth.py                # Autenticação e geração de tokens JWT
│   │   ├── ai.py                  # Integração com API Gemini
│   │   ├── requirements.txt       # Dependências Python
│   │   ├── .env                   # Variáveis de ambiente (DATABASE_URL MySQL)
│   │   ├── test_connection.py     # Script para testar conexão MySQL
│   │   ├── create_tables.py       # Script para criar tabelas no MySQL
│   │   └── create_mysql_setup.sql # SQL para criar banco e usuário
│   └── run_server.py              # Script para rodar o servidor
└── frontend/                        # Frontend React + Vite
    ├── src/
    │   ├── main.jsx               # Ponto de entrada React
    │   ├── app.jsx                # Componente principal
    │   ├── app.css                # Estilos globais
    │   ├── index.css              # Estilos base
    │   └── api.js                 # Cliente HTTP para API
    ├── components/
    │   ├── Navbar.jsx             # Componente de navegação
    │   ├── Navbar.css             # Estilos da navbar
    │   ├── Card.jsx               # Componente de card
    │   └── Card.css               # Estilos do card
    ├── pages/
    │   ├── login.jsx              # Página de login
    │   ├── dashboard.jsx          # Página principal
    │   ├── auth.css               # Estilos de autenticação
    │   └── dashboard.css          # Estilos do dashboard
    ├── index.html                 # HTML principal
    ├── vite.config.js            # Configuração Vite
    └── package.json              # Dependências JavaScript
```

## 🚀 Instalação e Execução

### Backend
## 🚀 Instalação e Execução

### Backend

1. **Ativar ambiente virtual:**
   ```bash
   cd "c:\Users\User\Documents\Dev\DevMatch AI Assistente de Estudo para Devs"
   .\.venv\Scripts\activate
   ```

2. **Instalar dependências:**
   ```bash
   cd backend\app
   pip install -r requirements.txt
   ```

3. **Executar servidor:**
   ```bash
   cd ..
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```

   ✅ **Backend rodando em:** `http://127.0.0.1:8000`
   - Documentação interativa: `http://127.0.0.1:8000/docs`

### Frontend

1. **Instalar dependências:**
   ```bash
   cd frontend
   npm install
   ```

2. **Executar em desenvolvimento:**
   ```bash
   npm run dev
   ```

   ✅ O frontend rodará em: `http://localhost:5173`

3. **Build para produção:**
   ```bash
   npm run build
   ```

## 📋 Endpoints da API

### Autenticação
- `POST /auth/register` - Registro de novo usuário
- `POST /auth/login` - Login de usuário

### IA
- `POST /ai/plan` - Gerar plano de estudo
- `POST /ai/questions` - Gerar questões de prática
- `POST /ai/explain` - Explicar um erro ou conceito

### Histórico
- `GET /history` - Obter histórico de estudos do usuário

## 🔑 Variáveis de Ambiente

### Backend
Arquivo `.env` em `backend/app/`:
```
DATABASE_URL=mysql+pymysql://devuser:devpass@localhost:3306/devmatch
SECRET_KEY=sua-chave-secreta-aqui
GEMINI_API_KEY=sua-chave-api-gemini
```

## 🛠️ Tecnologias

**Backend:**
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Python-Jose (JWT)
- Passlib (Hashing de senhas)
- Google Gemini API
- PyMySQL (driver MySQL)

**Frontend:**
- React 18
- Vite
- Axios
- CSS3

## 🗄️ Banco de Dados

**MySQL:**
- Banco: `devmatch`
- Usuário: `devuser` / Senha: `devpass`
- Host: `localhost:3306`

**Scripts úteis:**
- `backend/app/test_connection.py` - Testar conexão com MySQL
- `backend/app/create_tables.py` - Criar tabelas no banco
- `backend/app/create_mysql_setup.sql` - Script SQL para setup

## 📝 Notas Importantes

- ✅ O banco de dados foi migrado para MySQL (antes SQLite)
- ✅ Backend foi separado da pasta `devmatch-ai/` (agora em `backend/`)
- ✅ CORS está configurado para aceitar requisições de `http://localhost:5173`
- ✅ Autenticação é feita via JWT tokens armazenados no localStorage
- ✅ A integração com Gemini AI requer uma API key válida

## 🔐 Segurança

- Senhas são hasheadas com bcrypt
- JWT é usado para autenticação
- CORS está configurado adequadamente
- Variáveis sensíveis devem estar em `.env`
- MySQL com usuário/senha configurado
# DevMatch-AI-Assistente-de-Estudo-para-Devs
# DevMatch-AI-Assistente-de-Estudo-para-Devs
