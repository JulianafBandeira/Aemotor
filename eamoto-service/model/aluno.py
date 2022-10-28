from model.pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
    
    def __repr__(self):
        return '<nome{}nascimento{}email{}telefone{}instituicaoDeEnsino{}curso{}matricula{}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
