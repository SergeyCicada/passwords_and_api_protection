from flask import Flask
from app.dao.model.user import User


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application

def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def load_data():
    user = User(username="root", password="random_password", role="admin")

    db.create_all()

    with db.session.begin():
        db.session.add_all([user])
