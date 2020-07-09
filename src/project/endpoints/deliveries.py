import requests
from functools import wraps
from flask import request, jsonify, Blueprint
from project import db
from project.models import Pedido
from project.schemas import pedido_schema


blueprint = Blueprint('pedidos', __name__)


def check_token():
    authorization = request.headers.get('Authorization')

    response = requests.get(
        'http://localhost:5000/token',
        headers={'Authorization': authorization}
    )

    if response.ok:
        return response.json()
    return False


def autenticar(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        check_response = check_token()
        if check_response is False:
            return 'Unauthorized', 401
        return f(check_response, *args, **kwargs)
    return wrapper


@blueprint.route('/deliveries', methods=['GET'])
@autenticar
def list(usuario):
    pedidos = Pedido.query.filter_by(usuario_id=usuario['id'])

    return jsonify(pedido_schema.dump(pedidos, many=True)), 200


@blueprint.route('/deliveries', methods=['POST'])
@autenticar
def create(usuario):
    print(usuario)
    datos = request.json
    datos['usuario_id'] = usuario['id']
    pedido = pedido_schema.load(datos)

    db.session.add(pedido)
    db.session.commit()

    return pedido_schema.dump(pedido), 201
