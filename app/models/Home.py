from system.core.model import Model
from flask import Flask

class Home(Model):
    def __init__(self):
        super(Home, self).__init__()

    def get_content(self):
        query = "SELECT * FROM posts ORDER BY updated_at DESC LIMIT 30"
        content = self.db.query_db(query)
        return content
