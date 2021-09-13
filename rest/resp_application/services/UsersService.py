from flask import jsonify
from models.User import User

class UsersService:
  def __init__(self, db):
    self.db = db

  def save(self, user_request):
    user = User(
      name = user_request['name'],
      email = user_request['email']
    )

    try:
      self.db.session.add(user)
      self.db.session.commit()

      return jsonify({'code': 201, 'body': {'message': 'User succesfully created!'}}), 201
    except Exception as e:
      return jsonify({'code': 500, 'body': {'message': e}}), 500

  def listAll(self):
    users = User.query.all()

    if len(users) > 0:
      resp_payload = []
      for u in users:
        resp_payload.append({
          'name': u.name,
          'email': u.email
        })
        
      return jsonify({'code': 200, 'body': {'message': resp_payload}}), 200
    else:
      return jsonify({'code': 404, 'body': {'message': 'User not found!'}}), 404
