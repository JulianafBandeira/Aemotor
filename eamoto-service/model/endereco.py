


class Endereco():
   
    def __init__(self,numero, cep, logradouro,complemento):
        self.cep = cep
        self.numero = numero
        self.logradouro = logradouro
        self.complemento = complemento
        
    def __repr__(self):
       return '<logradouro{},cep{},numero{},complemento{}>'.format[self.logradouro,self.cep,self.complemento,self.numero]