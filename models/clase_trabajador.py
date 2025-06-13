from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

dbT=SQLAlchemy()

class trabajador(dbT.Model):
    __tablename__= 'trabajador'
    __id : Mapped[int] = mapped_column(primary_key=True)
    __apellido : Mapped[str] = mapped_column()
    __nombre : Mapped[str] = mapped_column() 
    __dni : Mapped[str] = mapped_column()
    __correo : Mapped[str] = mapped_column() 
    __legajo: Mapped[str] = mapped_column()
    __horas : Mapped[str] = mapped_column()
    __funcion : Mapped[str] = mapped_column()
        
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
    

