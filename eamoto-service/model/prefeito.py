
from model.pessoa import Pessoa



class Prefeito(Pessoa):
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return 'prefeito{}>'.format(self.pessoa)