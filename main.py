import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database= 'crudpython'
)

cursor = conexao.cursor()

#CRUD


"""
#CREATE
nome_produto = "lápis"
valor = 5
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #  Edita o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados

"""

"""
#READ
comando = f'SELECT * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)
"""


"""
#Update
nome_produto = "lápis"
valor = 1
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #  Edita o banco de dados
"""

#DELETE
nome_produto = "lápis"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()