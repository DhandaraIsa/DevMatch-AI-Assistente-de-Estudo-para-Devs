# DevMatch AI - Assistente de Estudo para Devs

Plataforma web inteligente que combina um backend FastAPI com um frontend React/Vite para criar um assistente de estudo alimentado por IA (Gemini).

## 📁 Estrutura do Projeto

```
DevMatch AI Assistente de Estudo para Devs/
├── .venv/                          # Ambiente virtual Python
├── devmatch-ai/
│   └── backend/
│       └── app/
│           ├── __init__.py
│           ├── main.py            # Aplicação FastAPI principal
│           ├── models.py           # Modelos SQLAlchemy (User, StudyItem)
│           ├── schemas.py          # Schemas Pydantic (validação de dados)
│           ├── database.py         # Configuração do banco de dados
│           ├── auth.py             # Autenticação e geração de tokens JWT
│           ├── ai.py               # Integração com API Gemini
│           └── requirements.txt    # Dependências Python
└── frontend/
    ├── public/
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

1. **Ativar ambiente virtual:**
   ```bash
   cd "c:\Users\User\Documents\Dev\DevMatch AI Assistente de Estudo para Devs"
   .\.venv\Scripts\activate
   ```

2. **Instalar dependências:**
   ```bash
   cd devmatch-ai\backend\app
   pip install -r requirements.txt
   ```

3. **Executar servidor:**
   ```bash
   cd ..
   python run_server.py
   ```

   ✅ **Backend rodando em:** `http://127.0.0.1:8003`
   - Documentação interativa: `http://127.0.0.1:8003/docs`

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

   O frontend rodará em: `http://localhost:5173`

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
Criar arquivo `.env` em `devmatch-ai/backend/app/`:
```
DATABASE_URL=sqlite:///./devmatch.db
SECRET_KEY=sua-chave-secreta-aqui
GEMINI_API_KEY=sua-chave-api-gemini
```

## 🛠️ Tecnologias

**Backend:**
- FastAPI
- SQLAlchemy
- Pydantic
- Python-Jose (JWT)
- Passlib (Hashing de senhas)
- Google Gemini API

**Frontend:**
- React 18
- Vite
- Axios
- CSS3

## 📝 Notas Importantes

- O banco de dados usa SQLite por padrão
- CORS está configurado para aceitar requisições de `http://localhost:5173`
- Autenticação é feita via JWT tokens armazenados no localStorage
- A integração com Gemini AI requer uma API key válida

## 🔐 Segurança

- Senhas são hasheadas com bcrypt
- JWT é usado para autenticação
- CORS está configurado adequadamente
- Variáveis sensíveis devem estar em `.env`
