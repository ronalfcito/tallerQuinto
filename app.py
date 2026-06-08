from flask import Flask
import psycopg2

app = Flask(__name__)

# NOTA: Para la Actividad 7, cambiarás este valor a "3.0.0"
VERSION = "2.0.0" 

@app.route("/")
def inicio():
    try:
        # 1. Establecer la conexión con la base de datos
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )

        cursor = conexion.cursor()

        # 2. Modificación: Consultar los datos de la tabla 'clientes'
        cursor.execute("SELECT id, nombre FROM clientes;")
        clientes = cursor.fetchall()  # Trae todas las filas de la tabla

        cursor.close()
        conexion.close()

        # 3. Formatear los clientes en una lista HTML
        lista_html = "<ul>"
        for cliente in clientes:
            lista_html += f"<li><strong>ID:</strong> {cliente[0]} - <strong>Nombre:</strong> {cliente[1]}</li>"
        lista_html += "</ul>"

        # Si no hay clientes registrados aún
        if not clientes:
            lista_html = "<p>No hay clientes registrados en la tabla.</p>"

        # 4. Retornar la interfaz web actualizada
        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>
        <hr>
        <h3>Lista de Clientes Registrados:</h3>
        {lista_html}
        """

    except Exception as e:
        return f"<h3>Error de conexión o consulta:</h3><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)