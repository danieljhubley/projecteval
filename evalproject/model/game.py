from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func

from evalproject.model.meta import Base

class Game(Base):
    __tablename__ = "game"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    release_date = Column(DateTime)
    desc = Column(String(400))
    developer = Column(String(100))
    publisher = Column(String(100))
    trailer_url = Column(String(100))
    esrb_id = Column(Integer)
    genre_id = Column(Integer)
    added_by = Column(String(100))
    date_added = Column(DateTime, default=func.now())
    last_modified_by = Column(String(100))
    last_modified = Column(DateTime, default=func.now())
    
    def __init__(self, title='', desc='', developer='', publisher='', trailer_url='', added_by='', last_modified_by=''):
        self.title = title
        self.desc = desc
        self.developer = developer
        self.publisher = publisher
        self.trailer_url = trailer_url
        self.added_by = added_by
        self.last_modified_by = last_modified_by

    def __repr__(self):
        return "<Game('%s')" % self.title