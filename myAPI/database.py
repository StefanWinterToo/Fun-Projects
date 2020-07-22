from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_ECHO'] = True


# Change settings.json to
# {
#    "python.linting.pylintArgs": [
#        "--load-plugins",
#        "pylint-flask"
#    ]
# }

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    age = db.Column(db.Integer)

    # Returns printable version of object
    #def __repr__(self):
    #    return '<Person %r>' % self.username

# When running for the first time:
# db.create_all()

# Block Comment: shift + alt + a
""" admin = Person()
admin.username = "Stefan"
admin.age = 25
db.session.add(admin)
# Commit adds an id
db.session.commit() """

stefan = Person.query.filter_by(username = "Stefan").first()
print(stefan.id)
print(stefan.username)
print(stefan.age)

db.session.close()


