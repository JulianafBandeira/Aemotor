


class Rota():
    def __init__(self, nomeDestino, prefeitura, qtdalunos,veiculo,passageiro,horaSaida,horaChegada):
        self.nomeDestino = nomeDestino
        self.prefeitura = prefeitura
        self.qtdalunos = qtdalunos
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada =  horaChegada

        return '<prefeitura{}, nomeDestino{},qtdalunos{},veiculo{},passageiro{},horaSaida{}, horaChegada{}>'.format[self.prefeitura,self.nomeDestino,self.qtdalunos,self.veiculo,self.passageiro,self.horaSaida,self.horaChegada]