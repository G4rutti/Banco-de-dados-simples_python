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

id_update = input('Digite o ID que queira atualizar: ')
print('''
            .T_NOMECONTATO
            .T_TELEFONECONTATO
            .T_EMAILCONTATO''')
coluna = input('Digite a coluna que queira atualizar: ')
mudanca = input('Digite o que quer mudar: ')


### atualizar na tabela###
def atualizar(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print('Registro atualizado')



vsql = 'UPDATE tb_contatos SET '""+coluna+""" = '"""+mudanca+"""' WHERE N_IDCONTATO= """+id_update+""
atualizar(vcon,vsql)