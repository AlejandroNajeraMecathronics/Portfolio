import sqlite3

conn = sqlite3.connect("citas.db")
c = conn.cursor()

# Agregar columna doctor si no existe
try:
    c.execute("ALTER TABLE citas ADD COLUMN doctor TEXT")
except:
    print("La columna doctor ya existe")

conn.commit()
conn.close()
print("Base de datos actualizada ✅")
