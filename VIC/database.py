from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pandas as pd
from Converter import open_file, extract_user, extract_company, create_dataframe, append_company_dataframe, replace_mcap 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vic.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Change settings.json to
# {
#    "python.linting.pylintArgs": [
#        "--load-plugins",
#        "pylint-flask"
#    ]
# }

class IdeaModel(db.Model):
    __tablename__ = "IdeaModel"
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    longShort = db.Column(db.String(255))
    company = db.Column(db.String(255))
    date = db.Column(db.Date)
    mcap = db.Column(db.Integer)
    price = db.Column(db.String(255)) # To be fixed when I have internet access
    ticker = db.Column(db.String(255))


    # Returns printable version of object
    def __repr__(self):
        return '<IdeaModel %s>' % self.author

# Marshmallow serializes the data
class IdeaSchema(ma.Schema):
    class Meta:
        # Which fields do we want to expose?
        fields = ("author", "longShort", "company", "mcap", "price", "ticker")

# When running for the first time:
db.drop_all()
db.create_all()

data = open_file()
user_list = extract_user(data)
df = create_dataframe(user_list)
company_list = extract_company(data)
df = append_company_dataframe(company_list, df, data)

df.to_sql(name='IdeaModel', con=db.engine, index=False, if_exists='append')
print("Saved to database")

db.session.close()
