from app.database import db
from datetime import datetime
import uuid

class Clasification(db.Model):
    __tablename__ = "resultados"

    id = db.Column(db.String(36), primary_key = True, default = lambda:str(uuid.uuid4()))
    
    corredor_name = db.Column(db.String(30),unique=True,nullable=False)
    
    tipo_carrera = db.Column(db.String(30),unique=False,nullable=False)

    clasificacion = db.Column(db.Integer,unique=False,nullable=False)

    tiempo = db.Column(db.DateTime,nullable=False)