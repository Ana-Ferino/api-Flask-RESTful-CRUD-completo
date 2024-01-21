from models.database import db_session
from models.pessoas import Pessoas
from dtos.person import PersonDTO
from exceptions import PersonAlreadyExistsError, PersonNotExistsError


class PessoasServices:
    
    def get(self, name: str = None, id: int = None):
        if name:
            person = Pessoas.query.filter_by(nome=name).first()
        else:
            person = Pessoas.query.filter_by(id=id).first()
        return person if person else None

    def modify(self, name: str, new_data: PersonDTO):
        new_name = new_data.name
        new_age = new_data.age

        if new_name:
            new_name_already_exists = self.get(new_name)
            if new_name_already_exists:
                raise PersonAlreadyExistsError
        
        current_person = self.get(name)

        if current_person:
            if new_name:
                current_person.nome = new_name
            if new_age:
                current_person.idade = new_age
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise PersonNotExistsError

    def save(self, person: PersonDTO):
        person_already_exists = self.get(person.name)
        if person_already_exists:
            raise PersonAlreadyExistsError
        
        new_person = Pessoas(nome=person.name, idade=person.age)
        db_session.add(new_person)
        db_session.commit()
        db_session.close()

    def delete(self, person: PersonDTO):
        person_to_delete = self.get(person.name)

        if person_to_delete:
            db_session.delete(person_to_delete)
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise PersonNotExistsError