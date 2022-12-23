from model.aluno import Aluno


class Passageiro(Aluno):

    
    def __init__(self,aluno,cidadeDestino,cidadeOrigem):
        
        self.aluno = aluno
        self.cidadeOrigem = cidadeDestino
        self.cidadeDestino = cidadeOrigem
        return '<aluno{}, cidadeOrigem{},cidadeDestino{}>'.format(self.aluno,self.cidadeDestino,self.cidadeOrigem)