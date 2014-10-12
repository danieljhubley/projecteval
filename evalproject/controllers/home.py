import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from evalproject.model.meta import Session
import evalproject.model as model
from evalproject.lib.base import BaseController, render

from sqlalchemy.sql import and_, or_, not_

log = logging.getLogger(__name__)

class HomeController(BaseController):

    def main(self):
        return render('/index.html/')

    def search(self, query):
        query = query.replace("'", "''");
        keywords = re.sub("[^\w]", " ",  query).split()
        keywords = ["%" + word + "%" for word in keywords]

        columns = [model.Game.title, model.Game.desc]
        conditions = []
        for column in columns:
            for keyword in keywords:
                conditions.append(column.ilike(keyword))
        condition = or_(*conditions)
        game_q = Session.query(model.Game).filter(condition)
        c.games = game_q.all()
        return render("/ajax/gamelist.html")
        
