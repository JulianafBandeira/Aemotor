from flask_restful import fields


error_campos = {
    'codigo': fields.String(attribute='codigo'),
    'message': fields.String(attribute='mensagem')
}


'''
    Classe Error.
'''


class Error:
    def __init__(self, codigo, mensagem, detalhe):
        self.codigo = codigo
        self.mensagem = mensagem
        self.detalhe = detalhe

    def __str__(self):
        return '<Error %d, %r>' % (self.codigo, self.mensagem)
