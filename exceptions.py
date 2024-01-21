class BusinessRulesValidationError(Exception):
    def __init__(self, msg=None):
        if msg is not None:
            self.msg = msg
        super().__init__(self.msg)

class UserAlreadyExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Usuário já existe, informe outro nome.'):
        super().__init__(msg)

class UserNotExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Usuário informado não existe.'):
        super().__init__(msg)

class UnauthorizedModification(BusinessRulesValidationError):
    def __init__(self, msg='Somente o próprio usuário pode se modificar ou deletar.'):
        super().__init__(msg)

class PersonAlreadyExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Já existe uma pessoa com esse nome.'):
        super().__init__(msg)

class PersonNotExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Pessoa informada não existe.'):
        super().__init__(msg)

class ActivityAlreadyExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Já existe uma atividade com esse nome.'):
        super().__init__(msg)

class ActivityNotExistsError(BusinessRulesValidationError):
    def __init__(self, msg='Atividade informada não existe.'):
        super().__init__(msg)
