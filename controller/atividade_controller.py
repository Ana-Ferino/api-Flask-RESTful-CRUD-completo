from services.atividade_services import AtividadesServices
from services.pessoa_services import PessoasServices
from exceptions import ActivityAlreadyExistsError, ActivityNotExistsError, PersonNotExistsError
from dtos.login import LoginDTO
from dtos.activity import ActivityDTO
from flask_restful import Resource
from pydantic import ValidationError
from flask import request, current_app


class AtividadeController(Resource):
    def get(self):
        try:
            uri_parameters = ActivityDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))

            current_app.logger.info("GET activity performed by the user : {}".format(auth.Usuario))
            activity = AtividadesServices().get(uri_parameters.name)
            person = PessoasServices().get(id=uri_parameters.person_id)
            return 'Activity: {} - Person associated: {}'.format(activity.nome, person.nome), 200
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500

    def post(self):
        try:
            payload = request.get_json()
            auth = LoginDTO(token=request.headers.get('Authorization'))

            data = ActivityDTO(**payload)
            person = PessoasServices().get(name=data.person_name)
            if person:
                current_app.logger.info("POST activity performed by the user : {}".format(auth.Usuario))
                data.person_id = person.id
                AtividadesServices().save(data)
                return 'Successfully registered activity: {}'.format(data.name), 201
            raise PersonNotExistsError
        
        except ActivityAlreadyExistsError as aae:
            return 'ERROR: {}'.format(aae), 422
        except ValidationError as error:
            return {'errors': error.errors()}, 420
        except Exception as excp:
            return 'An error occurred: {}'.format(excp), 500

    def patch(self):
        try:
            uri_parameters = ActivityDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))

            activity_to_modify = uri_parameters.name
            data = request.environ.get('json', None)
            new_activity = ActivityDTO(**data)
            person = PessoasServices().get(name=new_activity.person_name)
            new_activity.person_id = person.id

            AtividadesServices().modify(name=activity_to_modify, new_activity=new_activity)

            message = 'Activity {} modified successfully by user {}.'.format(activity_to_modify, auth.Usuario)
            current_app.logger.info(message)
            return message, 200

        except ActivityAlreadyExistsError as aae:
            return 'ERROR: {}'.format(aae), 422
        except ActivityNotExistsError as ane:
            return '{}'.format(ane), 500
        except ValidationError as error:
            return {'errors': error.errors()}, 420
        except Exception as excp:
            return 'An error occurred: {}'.format(excp), 500

    def delete(self):
        try:
            uri_parameters = ActivityDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            
            AtividadesServices().delete(activity=uri_parameters)

            message = 'Activity {} successfully deleted by user {}'.format(uri_parameters.name, auth.Usuario)
            current_app.logger.info(message)
            return message, 200
        
        except ActivityNotExistsError as ane:
            return '{}'.format(ane), 500
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500
