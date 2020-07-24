from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class PersonModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    age = db.Column(db.Integer)

    # Returns printable version of object
    def __repr__(self):
        return f"Person(username={username})"

db.create_all()

# Needs to be used without a database
person_put_args = reqparse.RequestParser()
person_put_args.add_argument("id", type = int, help="Id of person", required = True)
person_put_args.add_argument("username", type = str, help="Username of person", required = True)
person_put_args.add_argument("age", type = int, help="Age of person", required = True)

# persons = {"Stefan": {"id": 0, "username": "stwi", "age": 25}, "Hans": {"id": 1, "username": "hansi", "age": 79}}

# How an object should be serialized
resource_fields = {
	'id': fields.Integer,
	'username': fields.String,
	'age': fields.Integer,
}

class Person(Resource):
    #marshal_with serializes the return value of below
    @marshal_with(resource_fields)
    def get(self, person_id):
        # return {'id': id, 'username': username, 'age': age}
        # Query the database
        result = PersonModel.query.filter_by(id = person_id).first()
        if not result:
            abort(404, message = "No person found!")
        return result
    
    @marshal_with(resource_fields)
    def put(self, person_id):
        args = person_put_args.parse_args()
        
        result = PersonModel.query.filter_by(id = person_id).first()
        if result:
            abort(409, message = "Person Id already taken...")
        
        person = PersonModel(id = person_id, username = args['username'], age = args['age'])
        db.session.add(person)
        db.session.commit()
        return person, 201

api.add_resource(Person, '/person/<int:person_id>')

# db.session.close()

if __name__ == '__main__':
    app.run(debug=True)