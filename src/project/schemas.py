from project import ma
from project.models import Pedido


class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedido
        load_instance = True


pedido_schema = PedidoSchema()
