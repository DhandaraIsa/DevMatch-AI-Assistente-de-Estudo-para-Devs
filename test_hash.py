import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend\app\.env"))

# Testa se conseguimos usar hash_password
try:
    from app.auth import hash_password
    print("✓ Importou hash_password com sucesso")
    
    # Tenta usar
    try:
        hashed = hash_password("test123")
        print(f"✓ Hash gerado: {hashed[:20]}...")
    except Exception as e:
        print(f"✗ Erro ao fazer hash: {e}")
        
except Exception as e:
    print(f"✗ Erro ao importar: {e}")
    import traceback
    traceback.print_exc()
-
