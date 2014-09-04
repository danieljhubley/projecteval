import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from evalproject.model.meta import Session
import evalproject.model as model
import evalproject.lib.helpers as h

from evalproject.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PlatformsController(BaseController):

    def all_platforms(self):
        platform_q = Session.query(model.Platform)
        c.platforms = platform_q.order_by(model.Platform.name).all()
        return render('/platformlist.html/')
    
    def platform_info(self, id):
        platform_q = Session.query(model.Platform)
        c.platform = platform_q.get(int(id))
        if(c.platform is None):
            abort(404)
        return render('/platform.html/')
