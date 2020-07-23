from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

person_put_args = reqparse.RequestParser()
person_put_args.add_argument("id", type = int, help="Id of person", required = True)
person_put_args.add_argument("username", type = str, help="Username of person", required = True)
person_put_args.add_argument("age", type = int, help="Age of person", required = True)

persons = {"Stefan": {"id": 0, "username": "stwi", "age": 25}, "Hans": {"id": 1, "username": "hansi", "age": 79}}

def abort_if_person_non_existing(name):
    if name not in persons:
        abort(404, message = "Could not find person!")

class Person(Resource):
    def get(self, name):
        # return {'id': id, 'username': username, 'age': age}
        abort_if_person_non_existing(name)
        return persons[name]
    
    def put(self, name):
        arg = person_put_args.parse_args()
        persons[name] = arg
        return persons[name], 201

api.add_resource(Person, '/person/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)

