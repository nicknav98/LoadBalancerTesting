from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.gyms import Gym
from schemas.gyms import GymSchema

gym_schema = GymSchema()
gym_list_schema = GymSchema(many=True)


class GymListResource(Resource):

    def get(self):
        gyms = Gym.get_all_published()

        return gym_list_schema.dump(gyms), HTTPStatus.OK


    def post(self):
        json_data = request.get_json()
        data, errors = gym_schema.load(data=json_data)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST
        gym = Gym(**data)
        gym.save()

        return gym_schema.dump(gym), HTTPStatus.CREATED


class GymResource(Resource):
    @jwt_optional
    def get(self, gym_id):
        gym = Gym.get_by_id(gym_id=gym_id)

        if gym is None:
            return {'message': 'gym not found'}, HTTPStatus.NOT_FOUND

        return gym_schema.dump(gym).data, HTTPStatus.OK

    @jwt_required
    def patch(self, gym_id):

        json_data = request.get_json()

        data, errors = gym_schema.load(data=json_data, partial=('gymName',))

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        gym = Gym.get_by_id(gym_id=gym_id)

        if gym is None:
            return {'message': 'Gym not found'}, HTTPStatus.NOT_FOUND

        gym.name = data.get('gymName') or gym.name
        gym.PricePerMonth = data.get('pricePerMonth') or gym.pricePerMonth

        gym.save()

        return gym_schema.dump(gym), HTTPStatus.OK

    @jwt_required
    def delete(self, gym_id):
        gym = Gym.get_by_id(gym_id=gym_id)

        if gym is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        gym.delete()

        return {}, HTTPStatus.NO_CONTENT


class GymPublishResource(Resource):

    @jwt_required
    def delete(self, gym_id):
        gym = Gym.get_by_id(gym_id=gym_id)

        if gym is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        gym.is_open = False
        gym.save()

        return {}, HTTPStatus.NO_CONTENT
