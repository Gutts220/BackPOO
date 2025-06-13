from datetime import datetime
from flask import Flask, request, render_template
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from controllers.gestor_registro_horario import gestor_registro
from controllers.gestor_trabajador import gestor_trabajador




app = Flask(__name__)
app.config('.env')