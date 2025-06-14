from models.models import database, registro
from controllers.gestor_trabajador import gestor_trabajador
from flask import request, jsonify
from datetime import datetime


class gestor_registro:
    __gt: gestor_trabajador
    def __init__(self, gt):
        self.__gt = gt
    def buscar_reg_fecha(self, fecha, trabajador):
        registro_encontrado = registro.query.filter(registro.fecha == fecha, registro.idtrabajador == trabajador).first()
        if registro_encontrado:
            return registro_encontrado
        else:
            return None
   
    def nuevo_registro_entrada(self):
        # el flujo es el siguiente, ve si el trabajador existe, ve si no hay un registro del mismo dia, registra 
        resultado = None
        trabajador = None
        nuevo_registro = None

        # dni = request.form['dni'] Descomentar para trabajar con formularios
        # dependencia = request.form['dependencia']
        data = request.get_json()
        dni = data.get("dni")
        dependencia = data.get("dependencia")
        legajo = data.get("legajo")
        trabajador = self.__gt.buscar_trabajador(legajo, dni)
        if trabajador:      #EL trabajador existe?
            fecha = datetime.today().date()
            hora_entrada = datetime.now().time()
            nuevo_registro = self.buscar_reg_fecha(fecha, trabajador) 
            if not nuevo_registro:  #no hay registro de este dia?
                nuevo_registro = registro(fecha = fecha, horaentrada = hora_entrada, horasalida = None, dependencia = dependencia, idtrabajador = trabajador)
                database.session.add(nuevo_registro)    #agrego el registro
                database.session.commit()
                resultado = jsonify({"Ok": "Registro creado correctamente"}), 201
            else:
                resultado = jsonify({"error": "Registro ya creado"}), 409 
        else:
            resultado = jsonify({"error": "Trabajador no encontrado"}), 404   
        return resultado
    
    def registro_salida(self):
        # el flujo es el siguiente, ve si el trabajador existe, ve si no hay una salida del mismo dia, registra 
        resultado = None
        trabajador = None
        registro_entrada = None
        # dni = request.form['dni'] Descomentar para trabajar con formularios
        # dependencia = request.form['dependencia']
        data = request.get_json()
        dni = data.get("dni")
        legajo = data.get("legajo")
        trabajador = self.__gt.buscar_trabajador(legajo, dni)   
        if trabajador:      #EL trabajador existe?
            fecha = datetime.today().date()
            hora_salida = datetime.now().time()
            registro_entrada = self.buscar_reg_fecha(fecha, trabajador)  
            if registro_entrada:      #Esta el registro de entrada?
                if registro_entrada.horasalida:     #Ya habia registrado salida?
                    resultado = jsonify({"error": "Salida ya registrada"}), 409 
                else:
                    registro_entrada.horasalida = hora_salida
                    database.session.commit()
                    resultado = jsonify({"Ok": "Salida registrada correctamente"}), 200
            else:
                resultado = jsonify({"error": "Registro de entrada no encontrado"}), 404 
        else:
            resultado = jsonify({"error": "Trabajador no encontrado"}), 404   
        return resultado
                