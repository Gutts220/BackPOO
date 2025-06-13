from datetime import datetime, time
from sqlalchemy import DateTime, Time, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class registro(db.Model):
    __tablename__= 'registro'
    id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[datetime] = mapped_column(DateTime)
    hora_entrada: Mapped[time] = mapped_column(Time)
    hora_salida: Mapped[time] = mapped_column(Time)
    dependencia: Mapped[str] = mapped_column()
    id_trabajador: Mapped[int] = mapped_column(ForeignKey("trabajador.id"))
    
    def get_fecha(self):
        return self.fecha
    
    def get_hora_entrada(self):
        return self.hora_entrada
    
    def get_hora_salida(self):
        return self.hora_salida
    
    def get_dependencia(self):
        return self.dependencia
    
    def get_id_trabajador(self):
        return self.id_trabajador