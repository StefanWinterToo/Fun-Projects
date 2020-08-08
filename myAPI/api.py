from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from database import PersonModel, PersonSchema

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

"""
person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
"""

resource_fields = {
    'id': fields.Integer,
	'username': fields.String,
	'age': fields.Integer,
}

#Create a new restful resource
class PersonListResource(Resource):
    #marshal_with serializes the return value of below
    @marshal_with(resource_fields)
    def get(self):
        # return {'id': id, 'username': username, 'age': age}
        # Query the database
        result = PersonModel.query.all()
        if not result:
            abort(404, message = "No person found!")
        return result

#Create a new restful resource
class PersonResource(Resource):
    @marshal_with(resource_fields)
    def get(self, username):
        # return {'id': id, 'username': username, 'age': age}
        # Query the database
        result = PersonModel.query.filter_by(username = username).first()
        if not result:
            abort(404, message = "No person found!")
        return result
"""
class PersonListResource(Resource):
    def get(self):
        persons = PersonModel.query.all()
        return persons_schema.dump(persons)
    
    def post(self):
        new_Person = PersonModel(
            username = request.json['username'],
            age = request.json['age']
        )
        db.session.add(new_Person)
        db.session.commit()
        return person_schema.dump(new_Person)


class PersonResource(Resource):
    def get(self, username):
        person = PersonModel.query.get_or_404(username)
        return person_schema.dump(person)

class AgeResource(Resource):
    def get(self, age):
        person = PersonModel.query.get_or_404(age)
        return person_schema.dump(person)
"""

# Register resource and add api endpoint
api.add_resource(PersonListResource, '/persons/')
api.add_resource(PersonResource, '/persons/<string:username>')
#api.add_resource(AgeResource, '/persons/<int:age>')

"""
# Needs to be used without a database
person_put_args = reqparse.RequestParser()
person_put_args.add_argument("id", type = int, help="Id of person", required = True)
person_put_args.add_argument("username", type = str, help="Username of person", required = True)
person_put_args.add_argument("age", type = int, help="Age of person", required = True)
"""


# db.session.close()

if __name__ == '__main__':
    app.run(debug=True)