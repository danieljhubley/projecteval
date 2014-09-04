from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from evalproject.model.meta import Base

class ESRB(Base):
    __tablename__ = "esrb"
    
    id = Column(Integer, primary_key=True)
    short_desc = Column(String(100))
    full_desc = Column(String(400))
    image_url = Column(String(100))
    
    def __init__(self, short_desc='', full_desc='', image_url=''):
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.image_url = image_url

    def __repr__(self):
        return "<ESRB('%s')" % self.full_desc