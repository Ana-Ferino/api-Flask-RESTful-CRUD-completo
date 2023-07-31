from models import Atividades, db_session, Pessoas


class AtividadesRepository(Atividades):
    def __init__(self, nome_atividade, pessoa):
        self.nome = nome_atividade
        self.pessoa = pessoa

    def get():
        atividades = AtividadesRepository.query.all()
        dados_por_atividade = [{'id': i.id, 
                                'nome': i.nome, 
                                'pessoa_id': i.pessoa_id, 
                                'pessoa': i.pessoa.nome} for i in atividades]
        db_session.close()
        return dados_por_atividade, 200

    def modify(id, nome_atividade, pessoa_id):
        try:
            pessoa_associada = Pessoas.query.filter_by(id=pessoa_id).first()
            atividade = AtividadesRepository.query.filter_by(id=id).first()
            if atividade:
                atividade.nome = nome_atividade
                atividade.pessoa = pessoa_associada
                db_session.commit()
                return {'status': 'sucesso', 'mensagem': 'atividade editada com sucesso.'}, 200
            db_session.close()
        except Exception:
            {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}

    def save(nome_atividade, pessoa_id):
        try:
            pessoa_associada = Pessoas.query.filter_by(id=pessoa_id).first()
            nova_atividade = AtividadesRepository(nome_atividade, pessoa_associada)
            db_session.add(nova_atividade)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'atividade adicionada com sucesso.'}, 200
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}

    def delete(id):
        try:
            atividade_a_deletar = AtividadesRepository.query.filter_by(id=id).first()
            db_session.delete(atividade_a_deletar)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'atividade excluída com sucesso.'}, 200
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}
