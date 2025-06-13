from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class trabajador(db.model):
    __id : int
    __apellido : str
    __nombre: str
    __dni : str
    __correo : str
    __legajo : int
    __horas: int
    __funcion : str
    
    __tablename__= 'usuario'
    
    def __init__(self, db):
        self.__id = db.Column(db.Integer, primary_key=True)
        self.__apellido = db.model(db.String(80), nullable=False)
        self.__nombre = db.model(db.String(80), nullable=False) 
        self.__dni = db.model(db.String(80), nullable=False) 
        self.__correo = db.model(db.String(80), nullable=False) 
        self.__legajo = db.model(db.Integer, nullable=False) 
        self.__horas = db.model(db.Integer) 
        self.__funcion = db.model(db.String(80), nullable=False) 
        
    def get_id(self):
        return self.__id
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get__dni(self):
        return self.__dni
    
    def get_correo(self):
        return self.__correo
    
    def get_legajo(self):
        return self.__legajo
    
    def get_horas(self):
        return self.__horas
    
    def get_funcion(self):
        return self.__funcion
    

