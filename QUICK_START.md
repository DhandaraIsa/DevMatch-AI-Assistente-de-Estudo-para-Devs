## 🚀 Guia de Execução Rápida - DevMatch AI

### Pré-requisitos
- Python 3.11+
- Node.js 16+ e npm
- Git (opcional)

---

## ▶️ BACKEND

### 1. Abrir Terminal PowerShell

### 2. Navegar para o diretório do projeto
```powershell
cd "c:\Users\User\Documents\Dev\DevMatch AI Assistente de Estudo para Devs"
```

### 3. Ativar ambiente virtual
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependências (primeira vez apenas)
```powershell
cd devmatch-ai\backend\app
pip install -r requirements.txt
```

### 5. Executar servidor FastAPI
```powershell
cd ..
python run_server.py
```

✅ **Backend rodando em:** `http://127.0.0.1:8003`
- Documentação interativa: `http://127.0.0.1:8003/docs`

---

## ▶️ FRONTEND

### 1. Abrir OUTRO Terminal PowerShell

### 2. Navegar para o diretório frontend
```powershell
cd "c:\Users\User\Documents\Dev\DevMatch AI Assistente de Estudo para Devs\frontend"
```

### 3. Instalar dependências (primeira vez apenas)
```powershell
npm install
```

### 4. Executar servidor de desenvolvimento Vite
```powershell
npm run dev
```

✅ **Frontend rodando em:** `http://localhost:5173`

---

## 🔧 Configuração Necessária

### Backend - Variáveis de Ambiente
Criar arquivo `.env` em `devmatch-ai/backend/app/`:

```
DATABASE_URL=sqlite:///./devmatch.db
SECRET_KEY=dev-secret-key-change-in-production
GEMINI_API_KEY=sua_chave_api_gemini_aqui
```

---

## ✅ Checklist Final

- [ ] Backend em `http://localhost:8000` ✅
- [ ] Frontend em `http://localhost:5173` ✅
- [ ] Banco de dados criado em `devmatch-ai/backend/app/devmatch.db`
- [ ] Dependências instaladas em ambos os lados
- [ ] CORS funcionando (frontend consegue chamar backend)
- [ ] Variáveis de ambiente configuradas

---

## 📂 Estrutura Confirmada

```
✅ devmatch-ai/backend/app/    - API FastAPI
✅ frontend/src/               - Código React
✅ frontend/components/        - Componentes reutilizáveis
✅ frontend/pages/             - Páginas (login, dashboard)
✅ .venv/                      - Ambiente Python
✅ README.md                   - Documentação completa
```

---

## 🆘 Troubleshooting

**Erro: Módulos Python não encontrados**
- Certifique-se que `.venv` está ativado
- Execute: `pip install -r requirements.txt`

**Erro: CORS não permite requisições**
- Frontend deve rodar em `http://localhost:5173`
- Verifique a configuração em `main.py`

**Erro: npm não encontrado**
- Instale Node.js em: https://nodejs.org/

**Erro: Porta 5173 já em uso**
- Execute em outra porta: `npm run dev -- --port 5174`

---

## 📚 Recursos Úteis

- FastAPI Docs: `http://localhost:8000/docs`
- Vite Docs: https://vitejs.dev/
- React Docs: https://react.dev/
- API Gemini: https://ai.google.dev/

---

**Projeto atualizado e pronto para desenvolvimento! 🎉**
