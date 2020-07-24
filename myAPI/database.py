from flask import Flask, jsonify
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

# When running for the first time:
db.create_all()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    age = db.Column(db.Integer)

    # Returns printable version of object
    #def __repr__(self):
    #    return f"Person(name={name})"


# Block Comment: shift + alt + a
admin = Person()
admin.username = "Stefan"
admin.age = 25
db.session.add(admin)
# Commit adds an id
db.session.commit()

# Query database
""" stefan = Person.query.filter_by(username = "Stefan").first()
print(stefan.id)
print(stefan.username)
print(stefan.age) """

records = Person.query.all()

for record in records:
    print(record.username)
    #print(record.__dict__['username'])
    #print(f"<id={record.id}, username={record.username}, age = {record.age}>")
    #print("")

db.session.close()