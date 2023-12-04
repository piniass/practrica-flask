from database import db
from sqlalchemy.sql import func

class Personaje(db.Model):
    
    __tablename__ = 'personajes'
         
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alterego = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(80), unique=True, nullable=False)
   
    
    def __init__(self, nombre, alterego, tipo):
        self.nombre = nombre
        self.alterego = alterego
        self.tipo = tipo

    def __repr__(self):
        return f'<Personaje {self.id}>: {self.nombre}, {self.alterego}'
    