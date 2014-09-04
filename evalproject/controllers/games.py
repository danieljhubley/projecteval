import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from evalproject.model.meta import Session
import evalproject.model as model
import evalproject.lib.helpers as h

from evalproject.lib.base import BaseController, render

log = logging.getLogger(__name__)

class GamesController(BaseController):

    def all_games(self):
        game_q = Session.query(model.Game)
        c.games = game_q.order_by(model.Game.title).all()
        return render('/gamelist.html/')
    
    def game_info(self, id):
        game_q = Session.query(model.Game)
        c.game = game_q.get(int(id))
        if(c.game is None):
            abort(404)
        return render('/game.html/')