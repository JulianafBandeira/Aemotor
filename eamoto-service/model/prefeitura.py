


class Prefeitura():
    def __init__(self, telefone,email):
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<email{},telefone>'.format[self.email,self.telefone]