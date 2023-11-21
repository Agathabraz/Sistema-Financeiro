import mysql.connector

# Conectando ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ag993590*",
    database="db_Clientes"
)
# Crie um cursor
cursor = conexao.cursor()
# Execute uma consulta de seleção
consulta = "SELECT * FROM tabela"
cursor.execute(consulta)

# Recupere os resultados
resultados = cursor.fetchall()

# Exiba os resultados
for linha in resultados:
    print(linha)

# Feche o cursor e a conexão
cursor.close()
conexao.close()


# Função para cadastrar um novo cliente
def cadastrar_cliente(nome, email, telefone):
    cursor = db.cursor()
    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    values = (nome, email, telefone)
    cursor.execute(sql, values)
    db.commit()
    print("Cliente cadastrado com sucesso!")

# Solicitar dados do cliente
nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
telefone = input("Digite o telefone do cliente: ")

# Chamar função para cadastrar o cliente
cadastrar_cliente(nome, email, telefone)

# Fechar conexão com o banco de dados
db.close()
