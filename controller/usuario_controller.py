from services.usuario_services import UsuariosServices
from services.auth.sessions import SessaoServices
from flask_restful import Resource
from exceptions import UserAlreadyExistsError, UserNotExistsError, UnauthorizedModification
from dtos.login import LoginDTO
from dtos.usuario import UsuarioDTO
from dtos.login import LoginDTO
from flask import request, current_app


class UsuariosController(Resource):
    def get(self):
        try:
            uri_parameters = UsuarioDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)
            
            if same_user:
                user_data = UsuariosServices().get(username=uri_parameters.login)
                
                current_app.logger.info("GET performed by the user : {}".format(user_data.login))
                return 'Username: {}'.format(user_data.login), 200
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500
    

    def patch(self):
        try:
            uri_parameters = UsuarioDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)
            
            if same_user:
                user_to_modify = uri_parameters.login  
                new_data_for_the_user = request.environ.get('json', None)
                UsuariosServices().modify(usuario_atual=user_to_modify, novo_usuario=UsuarioDTO(**new_data_for_the_user))

                message = 'User {} modified successfully to {}.'.format(user_to_modify, new_data_for_the_user['user'])
                current_app.logger.info(message)
                return message, 200

        except UserAlreadyExistsError as uae:
            return '{}'.format(uae), 500
        except UserNotExistsError as une:
            return '{}'.format(une), 500
        except UnauthorizedModification as um:
            return '{}'.format(um), 401
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500


    def delete(self):
        try:
            uri_parameters = UsuarioDTO(**request.args.to_dict())
            auth = LoginDTO(token=request.headers.get('Authorization'))
            same_user = SessaoServices().validate_user_on_request(auth, uri_parameters)

            if same_user:
                UsuariosServices().delete(usuario=uri_parameters)
                
                message = 'User {} successfully deleted.'.format(uri_parameters.login)
                current_app.logger.info(message)
                return message, 200
        
        except UserNotExistsError as une:
            return '{}'.format(une), 500
        except UnauthorizedModification as um:
            return '{}'.format(um), 401
        except Exception as error:
            return 'An error occurred: {}'.format(error), 500