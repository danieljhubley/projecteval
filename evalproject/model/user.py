from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func

from evalproject.model.meta import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    date_registered = Column(DateTime, default=func.now())
    last_login = Column(DateTime, default=func.now())
    session_id = Column(String(200))
    
    def __init__(self, username='', email='', password='', session_id=''):
        self.username = username
        self.email = email
        self.password = password
        self.session_id = session_id
        
    def __repr__(self):
        return "<User('%s')" % self.username