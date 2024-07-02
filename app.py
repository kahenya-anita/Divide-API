import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
import sentry_sdk
from flask_swagger_ui import get_swaggerui_blueprint


import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

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
    """
    Divide two integers
    ---
    tags:
      - Division
    parameters:
      - name: a
        in: body
        description: The first integer
        required: true
        schema:
          type: integer
          example: 10
      - name: b
        in: body
        description: The second integer
        required: true
        schema:
          type: integer
          example: 2
    responses:
      200:
        description: The result of the division
        schema:
          type: object
          properties:
            result:
              type: integer
              example: 5
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              example: You cannot divide by 0
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            error:
              type: string
              example: Database error
    """
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

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Division API"})

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5500)