from system.core.controller import *

class Homes(Controller):
    def __init__(self, action):
        super(Homes, self).__init__(action)
        self.load_model('Home')

    def home(self):
        # content = self.models['Home'].get_content()
        return self.load_view('home.html')
