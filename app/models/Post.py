from system.core.model import Model
from flask import Flask

class Post(Model):
    def __init__(self):
        super(Post, self).__init__()


    def publish_post(self, content):
        query = "INSERT INTO posts (post, user_id, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(content['post'], content['user_id'])
        self.db.query_db(query)
