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


### consulta a tabela###
def consultar(conexao,sql):
        c = conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado



vsql = 'SELECT * FROM tb_contatos'
res = consultar(vcon,vsql)

for r in res:
    print(r)