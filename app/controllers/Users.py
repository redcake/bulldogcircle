
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

    def index(self):
        print "****************************************"
        return self.load_view('login_and_registration.html')


    def register(self):
        name = request.form['name']
        name_as_list = name.split()
        first = name_as_list[0]
        last = name_as_list[1]
        first_name = first.capitalize()
        last_name = last.capitalize()


        info = {
            "first_name" : first_name,
            "last_name" : last_name,
            "bc_email" : request.form['bc_email'],
            "alt_email" : request.form['alt_email'],
            "password" : request.form['password'],
            "confirmed_password" : request.form['confirmed_password']
        }
        register_status = self.models['User'].create_user(info)
        if register_status['status'] == False:
            return self.load_view('login_and_registration.html', errors = register_status['errors'])
        else:
            session['current_user'] = register_status['user']
            return redirect('/home')



    def login(self):
        print "****************************************"
        info = {
            "bc_email" : request.form['bc_email'],
            "password" : request.form['password']
        }
        print "****************************************"
        login_status = self.models['User'].login_user(info)
        print "****************************************"
        if login_status:
            session['current_user'] = login_status
            print session['current_user']
            return redirect('/home')
        else:
            message = 'We do not have a user with that email and password'
            return self.load_view('login_and_registration.html', message=message)




