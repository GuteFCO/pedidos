from project import db
from sqlalchemy.sql import func


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creacion = db.Column(db.DateTime, default=func.now(), nullable=False)
    actualizacion = db.Column(db.DateTime, onupdate=func.now(), nullable=True)
    estado = db.Column(db.String, nullable=False)
    detalles = db.relationship('Detalle', backref='pedido')
    usuario_id = db.Column(db.Integer, nullable=False)


class Detalle(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    pedido_id = db.Column(db.Integer, db.ForeignKey(Pedido.id), nullable=False)
