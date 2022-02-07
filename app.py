from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api


from Config import Config

from extensions import db, jwt

from resources.workout import WorkoutListResource, WorkoutResource, WorkoutPublishResource
from resources.token import TokenResource, RefreshResource, RevokeResource, black_list
from resources.user import UserListResource, UserResource, MeResource, UserWorkoutListResource, UserActivateResource



def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in black_list


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(WorkoutListResource, '/workouts')
    api.add_resource(WorkoutResource, '/workouts/<int:workout_id>')
    api.add_resource(WorkoutPublishResource, '/workouts/<int:workout_id>/publish')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(UserWorkoutListResource, '/users/<string:username>/workouts')

    api.add_resource(MeResource, '/me')
    api.add_resource(UserActivateResource, '/users/activate/<string:token>')

    api.add_resource(TokenResource, '/token')
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')


if __name__ == '__main__':
    app = create_app()

    app.run(port=5050, debug=True)
