
class UserAlreadyExistsError(Exception):
    def __init__(self, msg='Usuário já existe, informe outro nome.'):
        super().__init__(msg)


class UserNotExistsError(Exception):
    def __init__(self, msg='Usuário informado não existe.'):
        super().__init__(msg)


class UnauthorizedModification(Exception):
    def __init__(self, msg='Somente o próprio usuário pode se modificar ou deletar.'):
        super().__init__(msg)