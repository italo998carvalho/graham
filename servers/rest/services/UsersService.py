import json
from models.User import User

class UsersService:
  def __init__(self, db):
    self.db = db

  def save(self, user_request):
    req = json.loads(user_request)
    user = User(
      req['name'],
      req['email']
    )

    try:
      self.db.session.add(user)
      self.db.session.commit()

      return json.dumps({'code': 201, 'body': {'message': 'User succesfully created!'}}), 201
    except Exception as e:
      return json.dumps({'code': 500, 'body': {'message': e}}), 500

  def listAll(self):
    users = User.query.all()

    if len(users) > 0:
      resp_payload = []
      for u in users:
        resp_payload.append({
          'name': u.name,
          'email': u.email
        })
        
      return json.dumps({'code': 200, 'body': {'message': resp_payload}}), 200
    else:
      return json.dumps({'code': 200, 'body': {'message': []}}), 200
