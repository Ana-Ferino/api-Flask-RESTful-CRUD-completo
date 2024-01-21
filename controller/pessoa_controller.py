from services.pessoa_services import PessoasServices
from services.auth.sessions import SessaoServices
from exceptions import PersonAlreadyExistsError, PersonNotExistsError, UnauthorizedModification
from dtos.login import LoginDTO
from dtos.person import PersonDTO
from flask_restful import Resource
from pydantic import ValidationError
from flask import request, current_app


class PessoasController(Resource):
    def get(self):
        try:
            uri_parameters = PersonDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)

            if same_user:
                person = PessoasServices().get(name=uri_parameters.name)

                current_app.logger.info("GET performed by the user : {}".format(person.nome))
                return 'Name: {} - Age: {}'.format(person.nome, person.idade), 200
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500
    
    def post(self):
        try:
            payload = request.get_json()
            auth = LoginDTO(token=request.headers.get('Authorization'))

            person = PersonDTO(**payload)
            current_app.logger.info("POST activity performed by the user : {}".format(auth.Usuario))

            PessoasServices().save(person)
            return 'Successfully registered person: {}'.format(person.name), 201
        
        except PersonAlreadyExistsError as pae:
            return 'ERROR: {}'.format(pae), 422
        except ValidationError as error:
            return {'errors': error.errors()}, 420
        except Exception as excp:
            return 'An error occurred: {}'.format(excp), 500

    def patch(self):
        try:
            uri_parameters = PersonDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)
            
            if same_user:
                person_ty_modify = uri_parameters.name
                new_data = request.environ.get('json', None)
                PessoasServices().modify(person_ty_modify, new_data=PersonDTO(**new_data))

                message = 'Person {} modified successfully.'.format(person_ty_modify)
                current_app.logger.info(message)
                return message, 200
            
        except PersonAlreadyExistsError as pae:
            return 'ERROR: {}'.format(pae), 422
        except PersonNotExistsError as pne:
            return '{}'.format(pne), 500
        except UnauthorizedModification as um:
            return '{}'.format(um), 401
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500

    def delete(self):
        try:
            uri_parameters = PersonDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)

            if same_user:
                PessoasServices().delete(person=uri_parameters)
                
                message = 'Person {} successfully deleted.'.format(uri_parameters.name)
                current_app.logger.info(message)
                return message, 200
        
        except PersonNotExistsError as pae:
            return '{}'.format(pae), 500
        except UnauthorizedModification as um:
            return '{}'.format(um), 401
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500
