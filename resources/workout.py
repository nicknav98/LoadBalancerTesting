from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.workout import Workout
from schemas.workout import WorkoutSchema

workout_schema = WorkoutSchema()
workout_list_schema = WorkoutSchema(many=True)


class WorkoutListResource(Resource):

    def get(self):
        workouts = Workout.get_all_published()

        return workout_list_schema.dump(workouts), HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json()
        current_user = get_jwt_identity()
        data, errors = workout_schema.load(data=json_data)
        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST
        workout = Workout(**data)
        workout.user_id = current_user
        workout.save()

        return workout_schema.dump(workout), HTTPStatus.CREATED


class WorkoutResource(Resource):
    @jwt_optional
    def get(self, workout_id):
        workout = Workout.get_by_id(workout_id=workout_id)

        if workout is None:
            return {'message': 'workout not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if workout.is_publish == False and workout_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return workout_schema.dump(workout).data, HTTPStatus.OK

    @jwt_required
    def patch(self, workout_id):

        json_data = request.get_json()

        data, errors = workout_schema.load(data=json_data, partial=('name',))

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        workout = Workout.get_by_id(workout_id=workout_id)

        if workout is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != workout.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workout.name = data.get('name') or workout.name
        workout.length = data.get('length') or workout.length
        workout.directions = data.get('directions') or workout.directions
        workout.body_part = data.get('body_part') or workout.body_part

        workout.save()

        return workout_schema.dump(workout), HTTPStatus.OK

    @jwt_required
    def delete(self, workout_id):
        workout = Workout.get_by_id(workout_id=workout_id)

        if workout is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != workout.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workout.delete()

        return {}, HTTPStatus.NO_CONTENT


class WorkoutPublishResource(Resource):
    @jwt_required
    def put(self, workout_id):

        workout = Workout.get_by_id(workout_id=workout_id)

        if workout is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != workout.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workout.is_publish = True
        workout.save()

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required
    def delete(self, workout_id):

        workout = Workout.get_by_id(workout_id=workout_id)

        if workout is None:
            return {'message': 'Workout not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != workout.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        workout.is_publish = False
        workout.save()

        return {}, HTTPStatus.NO_CONTENT