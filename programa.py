from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Mi primera app Docker con Python</h1>
    <h2>Creada por Braulio</h2>
    """

@app.route("/conexion")
def conexion():
    try:
        con = mysql.connector.connect(
            host="host.docker.internal",
            port=3306,
            user="root",
            password="123456",
            database="empresa"
        )

        if con.is_connected():
            con.close()
            return """
            <h1>Aplicación de Braulio</h1>
            <h2>Conexión exitosa a la BD</h2>
            <p>MySQL está funcionando correctamente.</p>
            """

    except mysql.connector.Error as e:
        return f"""
        <h1>Aplicación de Braulio</h1>
        <h2>Error de conexión</h2>
        <p>{e}</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)