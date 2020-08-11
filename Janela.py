from iqoptionapi.stable_api import IQ_Option



import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [  [sg.Text('Valor 1'), sg.InputText(key=('login'),justification=('l'))],
            [sg.Text('Valor 2'), sg.InputText(key=('senha'),justification=('l'))],
            [sg.Text('Resultado',size=(100,2),justification=('c'))],
            [sg.Text(key='-saida-',text='0',size=(100,2),justification=('c'))],

            [sg.Button('Login'), sg.Button('Sair')]
            ]

# Create the Window

window = sg.Window('Calculadora', layout,size=(400,300))
window.read()
#window['-saida-'].update('21321132123132')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    else:
        API = IQ_Option(str(values['login']),str(values['senha']))
        API.connect()
        API.change_balance('PRACTICE')
        if API.check_connect()==True:
            window['-saida-'].update(str('Conectado com Suceso!'))
            pass
        else:
            window['-saida-'].update(str('Falha na conexao!'))
            pass
    
        pass    
            
        #total = int(values[0]) + int(values[1]) 
      #  window['-saida-'].update(str(total))
        #print('O Total é', total)
        #print(layout)

window.close()