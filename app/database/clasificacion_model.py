from app.database import db
from datetime import datetime
import uuid

class Carrera(db.Model):
    __tablename__ = "carreras"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)   # e.g. "GP de España"
    fecha = db.Column(db.Date, nullable=False)
    ubicacion = db.Column(db.String(100))                # opcional
    resultados = db.relationship('Resultado', back_populates='carrera')

class Piloto(db.Model):
    __tablename__ = "pilotos"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(5))
    equipo = db.Column(db.String(50))

class Resultado(db.Model):
    __tablename__ = "resultados"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    posicion = db.Column(db.Integer)
    vueltas = db.Column(db.Integer)
    tiempo = db.Column(db.String(30))
    intervalo = db.Column(db.String(20))
    velocidad_promedio = db.Column(db.String(20))
    paradas = db.Column(db.Integer)
    retiro = db.Column(db.String(30))
    motor = db.Column(db.String(50))

    piloto_id = db.Column(db.String(36), db.ForeignKey('pilotos.id'))
    carrera_id = db.Column(db.String(36), db.ForeignKey('carreras.id'))

    piloto = db.relationship('Piloto')
    carrera = db.relationship('Carrera', back_populates='resultados')