
from iqoptionapi.stable_api import IQ_Option
import time

inicio = time.time()

API= IQ_Option('eder0782hotmail.com','iqo473pti116')


API.connect()
#print('Conctado com sucesso')
# API.change_balance('PRACTICE')







if API.check_connect() == True:
    print('Conctado com sucesso!')
    API.change_balance('PRACTICE')
else:
    print('Falha!')
    exit()
   
perfil = API.get_profile_ansyc()

print(perfil['name'])
print(API.get_balance())
final = time.time()
Tempo = final - inicio

print('Tempo : ' + str(Tempo) )



