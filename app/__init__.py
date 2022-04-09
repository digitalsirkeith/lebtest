import dotenv
dotenv.load_dotenv()

import flask
import os

app = flask.Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY=os.getenv('SECRET_KEY')
)

from app.routes import index
app.register_blueprint(index.bp)