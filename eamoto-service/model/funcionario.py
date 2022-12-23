
from model.pessoa import Pessoa


class Funcionario(Pessoa):

    
    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo
        return '<prefeitura{},cargo{}>'.format(self.cargo,self.prefeitura)