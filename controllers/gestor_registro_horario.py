from models.models import database, registro, trabajador
from controllers.gestor_trabajador import gestor_trabajador
from flask import request, jsonify, render_template
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
        legajo = request.form['legajo']
        dni = request.form['dni_ultimos4'] 
        dependencia = request.form['dependencia']
        trabajador = self.__gt.buscar_trabajador(legajo, dni)
        if trabajador:      #EL trabajador existe?
            fecha = datetime.today().date()
            hora_entrada = datetime.now().time()
            nuevo_registro = self.buscar_reg_fecha(fecha, trabajador) 
            if not nuevo_registro:  #no hay registro de este dia?
                nuevo_registro = registro(fecha = fecha, horaentrada = hora_entrada, horasalida = None, dependencia = dependencia, idtrabajador = trabajador)
                database.session.add(nuevo_registro)    #agrego el registro
                database.session.commit()
            else:
                raise TypeError("Registro ya creado")
        else:
            raise TypeError("Trabajador no encontrado")
        return resultado
    
    def registro_salida(self):
        # el flujo es el siguiente, ve si el trabajador existe, ve si no hay una salida del mismo dia, registra 
        resultado = None
        trabajador = None
        registro_entrada = None
        legajo = request.form['legajo']
        dni = request.form['dni_ultimos4'] 
        dependencia = request.form['dependencia']
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
    
    def consultar_registros_propios(legajo, dni_ultimos4, fecha_inicio=None, fecha_fin=None):
        
        t = trabajador.query.filter(
        trabajador.legajo == legajo,
        trabajador.dni.like(f"%{dni_ultimos4}")
        ).first()
        if not t:
            return render_template('error.html', error="Trabajador no encontrado o DNI incorrecto.")

        query = registro.query.filter_by(idtrabajador=t.id)
        if fecha_inicio and fecha_fin:
            query = query.filter(registro.fecha >= fecha_inicio, registro.fecha <= fecha_fin)
        registros = query.all()
        return render_template(
            "registros_propios.html",
            registros=registros
    )
     
    def validar_trabajador(legajo, dni_ultimos4):
        
        return trabajador.query.filter(
            trabajador.legajo == legajo,
            trabajador.dni.like(f"%{dni_ultimos4}")
        ).first()
     
            
    def informe_horas_trabajadas(legajo, fecha_inicio, fecha_fin, funcion, dependencia, dni_ultimos4):
        # Buscar el trabajador (ya validado)
        t = trabajador.query.filter(
            trabajador.legajo == legajo,
            trabajador.dni.like(f"%{dni_ultimos4}")
        ).first()
        if not t:
            return render_template('error.html', error="Trabajador no encontrado.")

        # Buscar registros por id_trabajador, fechas y dependencia
        registros = registro.query.filter(
            registro.idtrabajador == t.id,
            registro.fecha >= fecha_inicio,
            registro.fecha <= fecha_fin,
            registro.dependencia == dependencia
        ).all()

        detalle = []
        total_horas = 0
        for r in registros:
            if r.horaentrada and r.horasalida:
                delta = datetime.combine(r.fecha, r.horasalida) - datetime.combine(r.fecha, r.horaentrada)
                horas = delta.total_seconds() / 3600
                total_horas += horas
            else:
                horas = 0
            detalle.append({
                "apellido": t.apellido,
                "nombre": t.nombre,
                "fecha": r.fecha.strftime("%Y-%m-%d"),
                "horaentrada": r.horaentrada.strftime("%H:%M") if r.horaentrada else "",
                "horasalida": r.horasalida.strftime("%H:%M") if r.horasalida else "",
                "horas": horas
            })
        return render_template(
            "informe_horas.html",
            detalle=detalle,
            total_horas=total_horas
        )