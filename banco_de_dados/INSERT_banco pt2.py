import sqlite3
from sqlite3 import Error

### Conexão ###
def conexao_banco():
    caminho = 'C:\\Users\\davizete\\Desktop\\banco_de_dados\\agenda.db'
    con = None

    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon = conexao_banco()

nome = input('Digite seu nome: ')
telefone = input('Digite seu número de telefone: ')
email = input('Digite seu email: ')

vsql =  """ INSERT INTO tb_contatos(
    T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO
)  
VALUES( 
'"""+nome+"" "' , '""" +telefone+" ""' ,'""" +email+"" "');"""

def inserir(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as er:
        print(er)

inserir(vcon,vsql)