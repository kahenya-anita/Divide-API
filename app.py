from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

logging.basicConfig(filename='app.log', level=logging.INFO)

class Divide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Divide {self.a}, {self.b}, {self.result}>'

@app.route('/')
def index():
    return 'Hello world'

@app.route('/api/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        a = int(data.get('a'))
        b = int(data.get('b'))
        if b == 0:
            return jsonify({
                "error": "You cannot divide by 0"
            }), 400
        result = a // b
        new_result = Divide(a=a, b=b, result=result)
        db.session.add(new_result)
        db.session.commit()

        logging.info(f"Payload: {data}")
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Inputs must be integers"}), 400
    except KeyError:
        return jsonify({"error": "Missing input values"}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)