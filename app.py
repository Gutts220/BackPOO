from datetime import datetime
from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash
from controllers.gestor_registro_horario import gestor_registro
from controllers.gestor_trabajador import gestor_trabajador

from models.clase_trabajador import dbT

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dbT.init_app(app)

app.route('/')
app.route('/nuevo_trabajador', methods = ['GET','POST'])
