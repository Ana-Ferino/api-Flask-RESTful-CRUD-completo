from models.atividades import Atividades
from models.database import db_session
from dtos.activity import ActivityDTO
from exceptions import ActivityAlreadyExistsError, ActivityNotExistsError


class AtividadesServices:

    def get(self, name: str):
        activity = Atividades.query.filter_by(nome=name).first()
        return activity if activity else None

    def modify(self, name: str, new_activity: ActivityDTO):
        new_activity = new_activity.name
        person = new_activity.person_id

        if new_activity:
            activity_already_exists = self.get(new_activity)
            if activity_already_exists:
                raise ActivityAlreadyExistsError
        
        current_activity = self.get(name)

        if current_activity:
            if new_activity:
                current_activity.nome = new_activity
            if person:
                current_activity.pessoa_id = person
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise ActivityNotExistsError

    def save(self, activity: ActivityDTO):
        activity_already_exists = self.get(activity.name)
        if activity_already_exists:
            raise ActivityAlreadyExistsError
        
        new_activity = Atividades(nome=activity.name, pessoa_id=activity.person_id)
        db_session.add(new_activity)
        db_session.commit()
        db_session.close()

    def delete(self, activity: ActivityDTO):
        activity_to_delete = self.get(activity.name)

        if activity_to_delete:
            db_session.delete(activity_to_delete)
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise ActivityNotExistsError