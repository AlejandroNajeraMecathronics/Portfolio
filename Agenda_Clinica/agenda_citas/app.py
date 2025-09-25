from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectarnos a la BD
def get_db_connection():
    conn = sqlite3.connect("citas.db")
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal: formulario de pacientes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        doctor = request.form["doctor"]

        # Si seleccionó "Cualquiera", asignar un doctor automáticamente
        if doctor == "Cualquiera":
            import random
            doctores = ["Dr. Ramírez", "Dra. López", "Dr. García"]
            doctor = random.choice(doctores)

        conn = get_db_connection()
        conn.execute("INSERT INTO citas (nombre, correo, fecha, hora, estado, doctor) VALUES (?, ?, ?, ?, ?, ?)",
                     (nombre, correo, fecha, hora, "Pendiente", doctor))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("index.html")

# Ruta del panel de administración
@app.route("/admin")
def admin():
    conn = get_db_connection()
    citas = conn.execute("SELECT * FROM citas").fetchall()
    conn.close()
    return render_template("admin.html", citas=citas)

if __name__ == "__main__":
    app.run(debug=True)
