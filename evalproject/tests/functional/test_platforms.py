from evalproject.tests import *

class TestPlatformsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='platforms', action='index'))
        # Test response...
