
from model.funcionario import Funcionario

class Motorista():

    
    def __init__(self, prefeitura, rotas, cargo):
        super().__init__(prefeitura, cargo)
        self.rotas = rotas
      
        return'<rotas{}prefeitura{}cargo{}>'.format(self.rotas, self.prefeitura, self.cargo)