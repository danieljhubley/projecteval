from sqlalchemy import Column
from sqlalchemy.types import Integer

from evalproject.model.meta import Base

class Gameplatform(Base):
    __tablename__ = "gameplatform"
    
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    platform_id = Column(Integer)
    
    def __init__(self):
        pass

    def __repr__(self):
        return "<Gameplatform('%s')" % self.id