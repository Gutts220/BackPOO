import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template
from models.models import database
from controllers.gestor_trabajador import gestor_trabajador
from controllers.gestor_registro_horario import gestor_registro


load_dotenv()

ruta = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database.init_app(app)


GT = gestor_trabajador()
GR = gestor_registro(GT)

@app.route("/")  # Marcador de server corriendo
def intex():
    return """SERVER IS RUNNING 
Hola adriano <3."""

@app.route('/nuevo_trabajador', methods=['GET','POST']) # Ruta para agregar trabajador
def nuevo_trabajador():
    return "Vista en construcción"

@app.route('/registrar_entrada', methods=['POST']) # Ruta para agregar registro de trabajadors
def registrar_entrada():
    return GR.nuevo_registro_entrada()

@app.route('/registrar_salida', methods=['POST']) # Ruta para agregar registro de trabajadors
def registrar_salida():
    pass


if __name__ == '__main__':
	app.run(debug = True)	