from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)

  def __init__(self, name, email):
    self.name = name
    self.email = email
