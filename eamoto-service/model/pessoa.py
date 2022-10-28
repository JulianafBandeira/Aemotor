
class Pessoa():

    def __init__(self, nome, nascimento, email, telefone):
        
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
       return '<nome{}, nascimento{}, email{}, telefone{}>'.format[self.nome,self.nascimento,self.email,self.telefone]