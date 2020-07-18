from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/database.db'
db = SQLAlchemy(app)

class IdeaModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(100), nullable = False)
    longShort = db.Column(db.String(10), nullable = False)
    company = db.Column(db.String(100), nullable = False)

    #def __repr__(self):
	#	return f"Idea(author = {author}, longShort = {longShort}, company = {company}"

idea_put_args = reqparse.RequestParser()
idea_put_args.add_argument("author", type = str, required = True, help = "Name of Author")
idea_put_args.add_argument("longShort", type = str, required = True, help = "Name of Author")
idea_put_args.add_argument("company", type = str, required = True, help = "Name of Author")

# db.create_all()

resource_fields = {
    "id": fields.Integer,
    "author": fields.String,
    "longShort": fields.String,
    "company": fields.String
}

class Idea(Resource):
    @marshal_with(resource_fields)
    def put(self, idea_id):
        args = idea_put_args.parse_args()
        result = IdeaModel.query.filter_by(id=idea_id).first()
        idea = IdeaModel(id = idea_id, author = args["author"], longShort = args["longShort"], company = args["company"])
        db.session.add(idea)
        db.session.commit()
        return idea

    @marshal_with(resource_fields)
	def get(self, idea):
		result = IdeaModel.query.filter_by(id=idea_id).first()
		if not result:
			abort(404, message="Could not find idea with that id")
		return result

api.add_resource(Idea, "")

if __name__ == "__main__":
	app.run(debug=True)