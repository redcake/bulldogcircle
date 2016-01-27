from system.core.model import Model
import re
from flask import Flask
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        BC_EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[bellevuecollege]+\.[edu]*$')
        ALT_EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        errors = []
        if not info['first_name']:
            errors.append('First name cannot be blank!')
        elif len(info['first_name']) < 2:
            errors.append('Name must be at least 2 characters long')

        if not info['last_name']:
            errors.append('Last name cannot be blank')
        elif len(info['last_name']) < 2:
            erorrs.append('Last name must be at least 2 characters long')


        if not info['bc_email']:
            errors.append('Email cannot be blank')
        elif not BC_EMAIL_REGEX.match(info['bc_email']):
            errors.append('You must have a bellevue college email')


        if len(info['alt_email']) > 0:
            if not ALT_EMAIL_REGEX.match(info['alt_email']):
                errors.append('Invalid alternate email')

        if not info['password']:
            errors.append('Password cannt be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be greater than 7 characters')
        elif info['password'] != info['confirmed_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status" : False, "errors" : errors}
        else:
            encrypted_password = bcrypt.generate_password_hash(info['password'])
            insert_query = "INSERT INTO users (first_name, last_name, bc_email, alt_email, user_level, encrypted_password, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', NOW(), NOW())".format(info['first_name'], info['last_name'], info['bc_email'], info['alt_email'], 1, encrypted_password)
            self.db.query_db(insert_query)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {"status" : True, "user" : user[0]}



    def login_user(self, info):
        print "****************************************"
        user_query = "SELECT * FROM users WHERE bc_email = '{}' LIMIT 1".format(info['bc_email'])
        user = self.db.query_db(user_query)
        if user:
            if self.bcrypt.check_password_hash(user[0]['encrypted_password'], info['password']):
                return user[0]
        return False











