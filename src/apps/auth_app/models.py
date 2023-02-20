from sqlalchemy import Column, Integer, String
from database import Base
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    username = Column(String(120))
    password_hash = Column(String(150))

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)
    
    
    def check_password(self, value):
        return check_password_hash(self.password_hash, value)

    def __repr__(self):
        return self.username
