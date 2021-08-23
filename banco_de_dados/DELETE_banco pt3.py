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

id_delete = input('Digite o id que deseja deletar: ')

### deletar na tabela###
def deletar(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print('Registro removido')



vsql = 'DELETE FROM tb_contatos WHERE N_IDCONTATO='"" +id_delete+""
deletar(vcon,vsql)