from flask import Flask
from database import db
from config import PORT
from views.UsersView import user

def create_app(db):
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://comm-tests:comm-tests@localhost:15432/comm-tests'
  app.secret_key = '123456789'

  db.init_app(app)

  app.register_blueprint(user)

  return app

def setup_database(app):
  with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app = create_app(db)
  setup_database(app)
  app.run(host='0.0.0.0', port=PORT, debug=True)
