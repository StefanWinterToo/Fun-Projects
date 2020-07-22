from flask import Flask, jsonify

app = Flask(__name__)

persons = [
    {
        'id': 0,
        'username': "Hans",
        'age': 25
    },
    {
        'id': 1,
        'username': "Peter",
        'age': 79
    }
]

## API ##
@app.route('/')
def get_person_name():
    print(jsonify({'persons': persons}))

if __name__ == '__main__':
    app.run(debug=True)

