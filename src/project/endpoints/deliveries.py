from flask import request, jsonify, Blueprint
from project import db
from project.models import Pedido
from project.schemas import pedido_schema


blueprint = Blueprint('pedidos', __name__)


@blueprint.route('/deliveries', methods=['GET'])
def list():
    pedidos = Pedido.query.all()

    return jsonify(pedido_schema.dump(pedidos, many=True)), 200


@blueprint.route('/deliveries', methods=['POST'])
def create():
    pedido = pedido_schema.load(request.json)

    db.session.add(pedido)
    db.session.commit()

    return pedido_schema.dump(pedido), 201
