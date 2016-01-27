from system.core.controller import *

class Posts(Controller):
    def __init__(self, action):
        super(Posts, self).__init__(action)
        self.load_model('Post')



    def post(self):
        print "********************* Posts#post *******************"
        post = request.form['post']
        content = {
            "user_id" : session['current_user']['id'],
            "post" : post
        }
        self.models['Post'].publish_post(content)
        return redirect('/home')

