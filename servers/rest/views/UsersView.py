from flask import Blueprint, request
from services.UsersService import UsersService
from database import db

user = Blueprint('user', __name__)
service = UsersService(db)


@user.route('/user', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        req_payload = request.get_json()

        return service.save(req_payload)

    else:
        return service.listAll()
