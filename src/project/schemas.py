from marshmallow import fields
from project import ma
from project.models import Pedido, Detalle


class PedidoSchema(ma.SQLAlchemyAutoSchema):
    detalles = fields.Nested('DetalleSchema', default=[], many=True)

    class Meta:
        model = Pedido
        load_instance = True


class DetalleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Detalle
        load_instance = True


pedido_schema = PedidoSchema()
detalle_schema = DetalleSchema()
