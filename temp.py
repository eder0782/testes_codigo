# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time, json
from iqoptionapi.stable_api import IQ_Option





while True:
    print("CONECÇÃO COM A IQ OPTION")
    email = input('Digite o seu email: ')
    senha = input('Digite a senha: ')
    API = IQ_Option(email, senha)
    API.connect()
    
   # conectado =API.check_connect()
    tentativas =0
    
    if API.check_connect() == False:        
        while API.check_connect() == False :
            print('Falha ao tentar se conectar!')
            API.connect()
            tentativas+=1
  
    else:
        ('Conexão realizada com sucesso!')
    
    
    def dados_peril(x):
        perfil = json.load(json.dumps(API.get_profile_ansyc()))
        return perfil[x]
        
    def converter_data(data_conv):
        hora = datetime.fromtimestamp(data_conv)
  
    informa = input('Digite 1 para pegar o nome do titular, 2 para pegar o saldo da conta'+
                    'e 3 para pegar a data de criação da conta: ')
    if informa =='1':
        print('O nome do titular da conta é: \n'+ dados_peril('name') )
    elif informa =='2':
        print('O saldo atual da conta é: \n'+ API.get_balance())
    elif informa =='3':
        print('A data da criação é \n'+ converter_data(dados_peril('crated')))    
    else:
        print('Opção inválida!!')
    
    sair = input('Deseja encerrar o programa( y/n) :')
    
    if sair =='y' or sair == 'Y':
        print('Encerrando o programa!')
        time.sleep(3)
        break
        
  

print

email = input('Digite o seu email: ')

API = IQ_Option(email, password)

