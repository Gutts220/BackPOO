import os
from dotenv import load_dotenv
from datetime import datetime
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
    return render_template('index.html')

@app.route('/nuevo_trabajador', methods=['GET','POST']) # Ruta para agregar trabajador
def nuevo_trabajador():
    return "Vista en construcción"

@app.route('/registrar_entrada', methods=['POST']) # Ruta para agregar registro de trabajadors
def registrar_entrada():
    return GR.nuevo_registro_entrada()

@app.route('/registrar_salida', methods=['POST']) # Ruta para agregar registro de trabajadors
def registrar_salida():
    return GR.registro_salida()

@app.route('/Informe_propio')
def informe_propio():
    return render_template('Informe_propio.html')

@app.route('/formulario_validacion')
def informe_horario_trabajadores():
    return render_template('formulario_validacion.html')


@app.route('/registros')
def ver_registros():
    legajo = request.args.get('legajo')
    dni_ultimos4 = request.args.get('dni_ultimos4')
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    if not legajo or not dni_ultimos4:
        return render_template('error.html', error="Faltan datos para la búsqueda.")
    return gestor_registro.consultar_registros_propios(legajo, dni_ultimos4, fecha_inicio, fecha_fin)

@app.route('/informe_horas', methods=['GET', 'POST'])
def informe_horas():
    if request.method == 'POST':
        # Primer paso: validar legajo y DNI
        legajo = request.form.get('legajo')
        dni_ultimos4 = request.form.get('dni_ultimos4')
        trabajador = gestor_registro.validar_trabajador(legajo, dni_ultimos4)
        if not trabajador:
            return render_template('error.html', error="Legajo o DNI incorrecto.")
        # Si es válido, mostrar el segundo formulario
        return render_template('formulario_periodo.html', legajo=legajo, dni_ultimos4=dni_ultimos4)
    else:
        # Mostrar el primer formulario
        return render_template('formulario_validacion.html')
    
@app.route('/mostrar_informe', methods=['POST'])
def mostrar_informe():
    legajo = request.form.get('legajo')
    dni_ultimos4 = request.form.get('dni_ultimos4')
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_fin = request.form.get('fecha_fin')
    funcion = request.form.get('funcion')
    dependencia = request.form.get('dependencia')

    # Buscar el trabajador 
    trabajador = gestor_registro.validar_trabajador(legajo, dni_ultimos4)
    if not trabajador:
        return render_template('error.html', error="Trabajador no encontrado.")

    # Verificar función y dependencia
    if trabajador.funcion != funcion:
        return render_template('error.html', error="La función no coincide con la registrada para el trabajador.")
    
    # Ahora sí, mostrar el informe (filtrando por legajo, fechas y dependencia)
    return gestor_registro.informe_horas_trabajadas(
        legajo, fecha_inicio, fecha_fin, funcion, dependencia, dni_ultimos4
    )

if __name__ == '__main__':
	app.run(debug = True)	