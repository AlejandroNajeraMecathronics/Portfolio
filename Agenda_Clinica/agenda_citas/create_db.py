import sqlite3

conn = sqlite3.connect("citas.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Base de datos creada con éxito ✅")
