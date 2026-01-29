# 🚀 DevMatch AI - Guia de Uso Rápido

## ✅ Status Atual (Janeiro 2025)

```
✅ Backend FastAPI ............ Rodando em http://localhost:8000
✅ Frontend React ............ Rodando em http://localhost:5173
✅ MySQL Database ............ Conectado (devmatch)
✅ Autenticação JWT ........... Funcionando (Argon2)
⏳ Google Gemini API ......... Modo Mock Ativo (quota reset necessário)
```

## 🎯 Como Acessar

### 1. Abrir Frontend
```
http://localhost:5173
```

### 2. Fazer Login
**Usuário de Teste:**
- Email: `test@devmatch.ai`
- Senha: `12345`

### 3. Dashboard
- Gerar plano de estudo
- Criar questões de revisão
- Explicar erros (feedback automático)

## 🔧 Reiniciar Serviços

### Terminal 1: Backend (se parou)
```bash
cd backend
python run_server.py
```

### Terminal 2: Frontend (se parou)
```bash
cd frontend
npm run dev
```

### Terminal 3: MySQL (se parou)
```bash
# Windows
net start MySQL80

# Ou verificar via:
mysql -u devuser -p -h localhost
# Senha: devpass
```

## 📱 Criar Novo Usuário

### Via API (cURL)
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "novo@email.com",
    "password": "senha123"
  }'
```

### Via Python
```python
import requests

response = requests.post(
    'http://localhost:8000/api/auth/register',
    json={
        'email': 'novo@email.com',
        'password': 'senha123'
    }
)
print(response.json())
```

## 🤖 Testar Gemini AI

### Quando Quota Resetar:
1. Editar `backend/app/.env`:
   ```
   USE_MOCK_AI=false
   ```

2. Reiniciar backend:
   ```
   python run_server.py
   ```

3. Testar endpoint:
   ```bash
   curl -X POST http://localhost:8000/api/ai/study-plan \
     -H "Authorization: Bearer SEU_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "topic": "Python",
       "level": "iniciante"
     }'
   ```

### Modo Mock (Atual - Offline)
```python
# ai.py está retornando respostas mock realistas
# Sem consumir API quota
# Perfeito para teste/desenvolvimento
```

## 📊 Endpoints Disponíveis

### Autenticação
- `POST /api/auth/register` - Criar novo usuário
- `POST /api/auth/login` - Login (retorna token JWT)

### AI (IA)
- `POST /api/ai/study-plan` - Gerar plano de estudo
- `POST /api/ai/questions` - Gerar questões de revisão
- `POST /api/ai/explain` - Explicar erro/conceito

### Health Check
- `GET /api/health` - Verificar se backend está rodando

## 🐛 Troubleshooting

### "Backend não conecta"
```bash
# Verificar se está rodando
netstat -ano | findstr 8000

# Se não, iniciar:
cd backend && python run_server.py
```

### "Frontend não carrega"
```bash
# Verificar se está rodando
netstat -ano | findstr 5173

# Se não, iniciar:
cd frontend && npm run dev
```

### "Login falha"
```bash
# Verificar credenciais
# Email: test@devmatch.ai
# Senha: 12345

# Ou criar novo usuário via API
```

### "Gemini API falha"
```bash
# Verificar .env
USE_MOCK_AI=true   # Modo offline
# ou
USE_MOCK_AI=false  # Quando quota resetar
```

### "Erro no banco de dados"
```bash
# Verificar MySQL está rodando
net start MySQL80

# Conectar ao banco
mysql -u devuser -p -h localhost
> use devmatch;
> show tables;
```

## 📈 Estrutura de Pastas

```
├── backend/
│   ├── app/
│   │   ├── ai.py ................. IA (Gemini/Mock)
│   │   ├── auth.py ............... Autenticação (JWT/Argon2)
│   │   ├── database.py ........... Conexão MySQL
│   │   ├── models.py ............. Modelos SQLAlchemy
│   │   ├── schemas.py ............ Schemas Pydantic
│   │   ├── main.py ............... Rotas FastAPI
│   │   ├── .env .................. Variáveis de ambiente
│   │   └── requirements.txt ....... Dependências
│   └── run_server.py ............. Iniciar servidor
│
├── frontend/
│   ├── src/
│   │   ├── app.jsx ............... Componente principal
│   │   ├── api.js ................ Cliente HTTP (Axios)
│   │   └── app.css ............... Estilos
│   ├── pages/
│   │   ├── login.jsx ............. Página de login
│   │   └── dashboard.jsx ......... Dashboard principal
│   ├── components/
│   │   ├── Card.jsx .............. Componente de card
│   │   └── Navbar.jsx ............ Barra de navegação
│   └── package.json .............. Dependências npm
│
└── docs/
    ├── README.md ................. Documentação geral
    ├── GEMINI_API_FIX.md ......... Documentação técnica
    ├── RESUMO_FINAL.md ........... Resumo executivo
    └── QUICK_START.md ............ Este arquivo
```

## 🎓 Próximas Features

- [ ] Upload de erros (arquivo de imagem/texto)
- [ ] Histórico de conversas
- [ ] Temas personalizados
- [ ] Integração com GitHub
- [ ] Exportar plano em PDF
- [ ] Modo dark/light

## 📞 Suporte

### Problemas Comuns
1. **Quota API excedida** → Usar modo mock até resetar
2. **Conexão MySQL falha** → Verificar service rodando
3. **Frontend em branco** → Limpar cache, `npm run dev`
4. **Token expirado** → Fazer login novamente

### Informações Úteis
- **API Key Gemini**: Configurada em `.env`
- **JWT Secret**: Alterado em produção
- **Database**: MySQL 8.0 em localhost:3306
- **Versão Python**: 3.14 recomendado

---

**Última atualização**: Janeiro 2025
**Desenvolvido com**: FastAPI + React + MySQL + Gemini AI
**Status**: ✅ Pronto para uso
