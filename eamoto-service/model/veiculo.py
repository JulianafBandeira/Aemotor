


class Veiculo():

    
    def __init__(self, cidade,qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa
        return '<cidade{}, qtdPassageiros{}, tipoVeiculo{}, placa{}>'.format(self.cidade,self.qtdPassageiros,self.tipoVeiculo,self.placa)
       