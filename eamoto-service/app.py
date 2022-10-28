from model.aluno import Aluno
from model.cidade import Cidade
from model.endereco import Endereco
from model.funcionario import Funcionario
from model.gestorapp import GestorApp
from model.instituicaoensino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo



aluno = Aluno("Coveira", "16/10/2000", "coveira.gmail", "7777-6666", "IFPB", "TSI", "6743332")
print(aluno) 

cidade = Cidade("Tacima", "TCM")
print(cidade)   

endereco = Endereco("58240-000", "20", "prédio", "sorveteria da esquina")
print(endereco)        
    
gestorapp = GestorApp("Dudão", "12/02/1999", "dudaogeorge@gmail", "9999-8888")
print(gestorapp)      

instituicaoensino = InstituicaoDeEnsino("IFPB", "beco das almas", "2409-3444")
print(instituicaoensino)  
    
motorista =  Motorista("Tacima", "Motorista")
print(motorista)    
       
passageiro = Passageiro (aluno, "Bananeiras", "Tacima")
print(passageiro)
 
pessoa =  Pessoa("Juliana", "14/08/1920", "juliana@hotmail", "1313-1313") 
print(pessoa)    
   
prefeito = Prefeito("LuisRodriguesXató", "20/09/1960", "xató@gmail", "7777-6666") 
print(prefeito)    

prefeitura = Prefeitura("Rodiguesxt", "Xatór@gmail.com", "4040-4040", "Borges")
print(prefeitura)  
   
funcionario = Funcionario(prefeitura, "Funcionario")
print(funcionario)  

rota = Rota("Tacima", "10", "Guarabira", "Onibus", "Paulo", "5:00", "7:00")
print(rota)      

uf = Uf("Paraíba","PB")
print(uf) 

veiculo = Veiculo("Tacima", "50", "Ônibus", "CVR-000")
print(veiculo)    
    
    
   