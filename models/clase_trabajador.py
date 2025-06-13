from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db=SQLAlchemy()

class trabajador(db.Model):
    __tablename__= 'trabajador'
    id : Mapped[int] = mapped_column(primary_key=True)
    apellido : Mapped[str] = mapped_column()
    nombre : Mapped[str] = mapped_column() 
    dni : Mapped[str] = mapped_column()
    correo : Mapped[str] = mapped_column() 
    legajo: Mapped[str] = mapped_column()
    horas : Mapped[str] = mapped_column()
    funcion : Mapped[str] = mapped_column()
        
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
    

