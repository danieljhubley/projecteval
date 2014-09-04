"""The application's model objects"""
from evalproject.model.meta import Session, Base

from evalproject.model.user import User
from evalproject.model.game import Game
from evalproject.model.platform import Platform
from evalproject.model.esrb import ESRB
from evalproject.model.genre import Genre
from evalproject.model.gameplatform import Gameplatform

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
