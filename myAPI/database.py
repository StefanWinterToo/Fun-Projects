from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
# app.config['SQLALCHEMY_ECHO'] = True

# Change settings.json to
# {
#    "python.linting.pylintArgs": [
#        "--load-plugins",
#        "pylint-flask"
#    ]
# }

class PersonModel(db.Model):
    __tablename__ = "PersonModel"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    age = db.Column(db.Integer)

    # Returns printable version of object
    def __repr__(self):
        return '<PersonModel %s>' % self.username

# Marshmallow serializes the data
class PersonSchema(ma.Schema):
    class Meta:
        # Which fields do we want to expose?
        fields = ("username", "age")

# When running for the first time:
db.drop_all()
db.create_all()

# Creates objects of PersonModel and ads to database
"""
# Block Comment: shift + alt + a
admin = PersonModel(username="Stefan", age=25)
dev = PersonModel(username="Hans",age=36)
db.session.add(admin)
db.session.add(dev)
# Commit adds an id
db.session.commit() 
"""

# Converts dataframe to objects and ads to database
data = {'username': ['Stefan', 'Maxi'], 'age': [25, 65]}
df = pd .DataFrame(data)
df.to_sql(name='PersonModel', con=db.engine, index=False, if_exists='append')

# Query database
""" stefan = PersonModel.query.filter_by(username = "Stefan").first()
print(stefan.id)
print(stefan.username)
print(stefan.age) """

db.session.close()