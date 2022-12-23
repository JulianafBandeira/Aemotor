


class InstituicaoDeEnsino():

    
    def __init__(self, nome, logradouro, telefone):
        self.nome = nome
        self.logradouro = logradouro
        self.telefone = telefone
        return '<nome{}, logradouro{},telefone{}>'.format(self.nome,self.logradouro,self.telefone)