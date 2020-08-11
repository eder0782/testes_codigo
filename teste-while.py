from threading import Thread
import time
from flask import Flask, render_template, jsonify
#from serialtest import get_dist
import multiprocessing




app = Flask(__name__)


'''

class Thread(threading.Thread):

    def __init__(self):
        super(Thread, self).__init__()
        self.kill = threading.Event()

    def run(self):
        # Enquanto a thread não estiver 'morta'
        contador()

    def stop(self):
        # Mata a thread
        print("thread parando.")
        self.kill.set()

'''
ativo = False

def contador():
   
    i=1
    #global ativo
    while True:
        print(i)
        i+=1
        time.sleep(1)

t=Thread(target=contador) 



def processo(arg):
    processo = multiprocessing.Process(target=contador)
    if arg=='start':
        processo.start()
    else:
        processo.terminate()


    

@app.route('/start')
def start():
    #modificavar('start')
    #global ativo
    
    #ativo = True
    
    processo('start')
    
    return 'start'

@app.route('/stop')
def stop():
    #global ativo
    #ativo = False
    #t._tstate_lock
    processo('stop')
    return 'stop'

@app.route('/')
def index():
    
    
    return 'Ola'


if __name__ == "__main__":
   
    app.run( debug=True, threaded=True)





