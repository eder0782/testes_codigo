# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:39:58 2020

@author: EDER
"""

from iqoptionapi.stable_api import IQ_Option

import time
from datetime import datetime
from dateutil import tz
import pandas
from pytz import timezone


API = IQ_Option('eder0782@hotmail.com', 'iqo473pti116')

API.connect()

API.change_balance('PRACTICE')

tentativas = 5

if API.check_connect() == False:
    while tentativas<=5:
        print('Falha ao tentar se conectar!')
        API.connect()
        tentativas+=1
else:
    print('Conexão realizada com sucesso!')
    
candle=API.get_candles('EURUSD', 60, 3, time.time())  



#data = candle[0]['from']

#data2 = datetime.fromtimestamp(data,tz= timezone('America/Manaus'))

#print(data2)
#print(pandas.Timestamp.tzname(pandas.Timestamp.today()))
#print(pandas.Timestamp(data, unit='s', tz='America/Sao Paulo'))


def converter_data(data_conv):
    hora = datetime.fromtimestamp(data_conv)
    
    return hora
       
for vela in candle:
    horario = converter_data(vela['from'])
    print('Horario: '+str(horario) +
          '| Valor Abertura: '+str(vela['open'])+
          '| Valor Fechamento: '+ str(vela['close']))




    