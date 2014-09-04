import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from evalproject.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HomeController(BaseController):

    def main(self):
        return render('/index.html/')
