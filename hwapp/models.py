from hwapp import login
from hwapp import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True )
    city_name = db.Column(db.String(64), index = True)
    city_rank = db.Column(db.Integer(), index = True)

    def __repr__(self):
        return '{}'.format(self.city_name)
    


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
