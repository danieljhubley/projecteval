"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    mcon = map.connect

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    mcon('/error/{action}', controller='error')
    mcon('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    mcon('/', controller='home', action='main')
    mcon('/search/:query', controller='home', action='search', conditions = dict(method=['POST', 'GET']))
    mcon('/games', controller='games', action='all_games')
    mcon('/games/:id', controller='games', action='game_info')
    mcon('/platforms', controller='platforms', action='all_platforms')
    mcon('/platforms/:id', controller='platforms', action='platform_info')

    return map
