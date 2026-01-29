import pymysql

conn = pymysql.connect(host='localhost', user='root')
cursor = conn.cursor()

try:
    cursor.execute("DROP USER IF EXISTS 'devuser'@'localhost'")
    conn.commit()
    print("✓ Usuário antigo removido")
except Exception as e:
    print(f"Erro ao remover usuário: {e}")

try:
    cursor.execute("CREATE USER 'devuser'@'localhost' IDENTIFIED BY 'devpass'")
    conn.commit()
    print("✓ Novo usuário criado")
except Exception as e:
    print(f"Erro ao criar usuário: {e}")

try:
    cursor.execute("GRANT ALL PRIVILEGES ON devmatch.* TO 'devuser'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")
    conn.commit()
    print("✓ Privilégios concedidos")
except Exception as e:
    print(f"Erro ao conceder privilégios: {e}")

cursor.close()
conn.close()
print("\n✅ Configuração do usuário MySQL concluída!")
-
