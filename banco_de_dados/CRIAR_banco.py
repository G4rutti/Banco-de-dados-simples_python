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

### Criar Tabela ###
vsql = '''CREATE TABLE tb_contatos(

        N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMECONTATO VARCHAR(100),
        T_TELEFONECONTATO VARCHAR(20),
        T_EMAILCONTATO VARCHAR(100)
);'''

def criar_tabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as er:
        print(er)


criar_tabela(vcon,vsql)
vcon.close()