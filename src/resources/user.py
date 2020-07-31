from flask_restful import Resource, reqparse
from src.models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'email', required=True, help='Email is required field'
    )
    parser.add_argument(
        'password', required=True, help='Password is required field'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        user = UserModel.find_by_email(data['email'])

        if user:
            return {'message': "User already exists"}, 400

        user = UserModel(data['email'], data['password'])
        user.save()

        return {'message': 'User is created'}, 201
