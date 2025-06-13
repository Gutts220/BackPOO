from datetime import datetime, time
from sqlalchemy import DateTime, Time, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class registro(db.Model):
    __tablename__= 'registro'
    __id: Mapped[int] = mapped_column(primary_key=True)
    __fecha: Mapped[datetime] = mapped_column(DateTime)
    __hora_entrada: Mapped[time] = mapped_column(Time)
    __hora_salida: Mapped[time] = mapped_column(Time)
    __dependencia: Mapped[str] = mapped_column()
    __id_trabajador: Mapped[int] = mapped_column(ForeignKey("trabajador.id"))
    
    def get_fecha(self):
        return self.__fecha
    
    def get_hora_entrada(self):
        return self.__hora_entrada
    
    def get_hora_salida(self):
        return self.__hora_salida
    
    def get_dependencia(self):
        return self.__dependencia
    
    def get_id_trabajador(self):
        return self.__id_trabajador