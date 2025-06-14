from datetime import datetime, time, date
from sqlalchemy import DateTime, Time, ForeignKey, Date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column


database = SQLAlchemy()

class registro(database.Model):
    __tablename__= 'registrohorario'
    id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[date] = mapped_column(Date)
    horaentrada: Mapped[time] = mapped_column(Time)
    horasalida: Mapped[time] = mapped_column(Time)
    dependencia: Mapped[str] = mapped_column()
    idtrabajador: Mapped[int] = mapped_column(ForeignKey("trabajador.id"))
    

class trabajador(database.Model):
    __tablename__= 'trabajador'
    id : Mapped[int] = mapped_column(primary_key=True)
    apellido : Mapped[str] = mapped_column()
    nombre : Mapped[str] = mapped_column() 
    dni : Mapped[str] = mapped_column()
    correo : Mapped[str] = mapped_column() 
    legajo: Mapped[str] = mapped_column()
    horas : Mapped[str] = mapped_column()
    funcion : Mapped[str] = mapped_column()