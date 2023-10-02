from flask_restful import Resource
from flask import request
from pydantic import ValidationError
from dtos.signup import SignUpRequestDTO
from services.usuario_services import UsuariosServices
from exceptions import UserAlreadyExistsError


class SignUpController(Resource):

    def post(self):
        try:
            payload = request.get_json()
            data = SignUpRequestDTO(**payload)
            UsuariosServices().save(data)
            return 'Successfully registered user: {}.'.format(data.usuario), 201

        except UserAlreadyExistsError as uae:
            return 'ERROR: {}'.format(uae), 422
        except ValidationError as error:
            return {'errors': error.errors()}, 420