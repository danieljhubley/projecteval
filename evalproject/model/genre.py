from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from evalproject.model.meta import Base

class Genre(Base):
    __tablename__ = "genre"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return "<Genre('%s')" % self.name