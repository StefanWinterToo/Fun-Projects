from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from database import IdeaModel, IdeaSchema

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vic.db'
db = SQLAlchemy(app)

resource_fields = {
    'id': fields.Integer,
    'author': fields.String,
    'longShort': fields.String,
    'company': fields.String,
    'mcap': fields.String,
    'price': fields.String,
    'ticker': fields.String
}

#Create a new restful resource
class IdeaListResource(Resource):
    #marshal_with serializes the return value of below
    @marshal_with(resource_fields)
    def get(self):
        # return {'id': id, 'username': username, 'age': age}
        # Query the database
        result = IdeaModel.query.all()
        if not result:
            abort(404, message = "No ideas found!")
        return result

#Create a new restful resource
class IdeaResource(Resource):
    @marshal_with(resource_fields)
    def get(self, author):
        # return {'id': id, 'username': username, 'age': age}
        # Query the database
        result = IdeaModel.query.filter_by(author = author).first()
        if not result:
            abort(404, message = "No author found!")
        return result

api.add_resource(IdeaListResource, '/ideas/')
api.add_resource(IdeaResource, '/ideas/<string:author>')

if __name__ == "__main__":
	app.run(debug=True)