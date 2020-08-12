import sqlite3 as sq
import sys

con = sq.connect('database.db')



con.execute(''' CREATE TABLE IF NOT EXISTS
 USUARIO(
    ID INTEGER PRIMARY KEY,
    NOME TEXT NOT NULL
);''')

con.commit()
#teste
cursor = con.cursor()

def listar():
    cursor.fetchone()   
    cursor.execute('SELECT * FROM USUARIO')
    for i in cursor:
        print(i)

def close():
    con.close()
    sys.exit()
    

def deletar(x):
     
    con.execute('Delete from usuario where id = ?',(x,))
    con.commit()

def update(id,nome):
    cursor.execute('update usuario set nome=? where id = ?',(nome,id))
    con.commit()
    


while True:
    opcao =input('Digite: 1 para fazer novo cadastro, 2 para consultar, 3 para deletar,4 para atualizar, e 5 sair:')
    
    
    if opcao == '1':
        id =input('Digite a id para cadastrar:')
        nome = input('Digite o nome:')
        con.execute('Insert into usuario values(?,?)',(id,nome))
        con.commit()
        continue
    elif opcao == '2':
        listar()
        continue
    elif opcao == '3':
        excluir  =input('Digite a ID para exluir:')
        deletar(excluir)
        continue
    elif opcao == '4':
        idmod  =input('Digite a ID para modificar o usuario:')
        nome_mod= input('Digite o novo mome do usuário: ')
        update(idmod,nome_mod)
        continue
    else:
        close()


















