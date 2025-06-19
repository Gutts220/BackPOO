from models.models import database, trabajador
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template

class gestor_trabajador:
    
    def nuevo_trabajador():   
        resultado= render_template('aviso.html', mensaje="No se pudo ejecutar la operación")
        if request.method == 'POST':
            if not request.form['nombre'] or not request.form['email'] or not request.form['password']:
                resultado=  render_template('error.html', error="Los datos ingresados no son correctos...")
            else:
                nuevo_trabajador = trabajador(nombre=request.form['nombre'], correo = request.form['email'], clave=generate_password_hash(request.form['password']))       
                database.session.add(nuevo_trabajador)
                database.session.commit()
                resultado=  render_template('aviso.html', mensaje="El trabajador se registró exitosamente")
        else:
            resultado= render_template('nuevo_trabajador.html')
        return resultado

    def buscar_trabajador(self, legajo,dni):
        trabajador_encontrado = trabajador.query.filter( trabajador.legajo == legajo, trabajador.dni.like(f"%{dni}")).first()
        print(trabajador_encontrado)
        
        if trabajador_encontrado:
            return trabajador_encontrado.id
        else:
            return None
                
    