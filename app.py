from datetime import datetime
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from controllers.gestor_registro_horario import gestor_registro
from controllers.gestor_trabajador import gestor_trabajador



load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/")
def intex():
    return """SERVER IS RUNNING 
Hola adriano <3."""
    

    

if __name__ == '__main__':
	app.run(debug = True)	