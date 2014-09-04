from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func

from evalproject.model.meta import Base

class Platform(Base):
    __tablename__ = "platform"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    release_date = Column(DateTime)
    desc = Column(String(1000))
    developer = Column(String(100))
    manufacturer = Column(String(100))
    cpu = Column(String(100))
    memory = Column(String(100))
    graphics = Column(String(100))
    storage = Column(String(100))
    added_by = Column(String(100))
    date_added = Column(DateTime, default=func.now())
    last_modified_by = Column(String(100))
    last_modified = Column(DateTime, default=func.now())
    
    def __init__(self, name='', desc='', developer='', manufacturer='', cpu='', memory='', graphics='', storage=''):
        self.name = name
        self.desc = desc
        self.developer = developer
        self.manufacturer = manufacturer
        self.cpu = cpu
        self.memory = memory
        self.graphics = graphics
        self.storage = storage

    def __repr__(self):
        return "<Platform('%s')" % self.name