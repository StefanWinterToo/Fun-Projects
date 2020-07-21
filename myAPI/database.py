from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
db.create_all()

admin = Person()
admin.id = 2
admin.username = "Peter"
admin.age = 99
db.session.add(admin)

db.session.commit()
db.session.close()


Person.query.all()