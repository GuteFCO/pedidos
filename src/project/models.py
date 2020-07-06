from project import db


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creacion = db.Column(db.String, nullable=False)
    actualizacion = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
