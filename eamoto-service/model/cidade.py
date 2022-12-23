


class Cidade():
   
    
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    def __repr__(self):
        return '<nome{},sigla{}>'.format(self.nome,self.sigla)