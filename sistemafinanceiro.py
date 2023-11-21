# Lista para armazenar os clientes
clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    nascimento = input("Digite sua Data de Nascimento")
    email = input("Digite o email do cliente: ")
    endereco = input("Digite seu Endereço")
    telefone = input("Digite o telefone do cliente: ")
    
    cliente = {
        "nome": nome,
        "nascimento": nascimento,
        "email": email,
        "endereco": endereco,
        "telefone": telefone
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def mostrar_clientes():
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Telefone: {cliente['telefone']}")
            print("-----------------------")

def atualizar_cliente():
    email = input("Digite o email do cliente que deseja atualizar: ")
    
    
    for cliente in clientes:
        if cliente["email"] == email:
            novo_email = input("Digite o novo email do cliente: ")
            novo_telefone = input("Digite o novo telefone do cliente: ")
            
            cliente["email"] = novo_email
            cliente["telefone"] = novo_telefone
            
            print("Cliente atualizado com sucesso!")
            return
    
    print("Cliente não encontrado.")

def excluir_cliente():
    email = input("Digite o email do cliente que deseja excluir: ")
    
    for cliente in clientes:
        if cliente["email"] == email:
            clientes.remove(cliente)
            print("Cliente excluído com sucesso!")
            return
    
    print("Cliente não encontrado.")

# Loop principal do programa
while True:
    print("===== CADASTRO DE CLIENTES =====")
    print("1 - Cadastrar cliente")
    print("2 - Mostrar clientes")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        mostrar_clientes()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        excluir_cliente()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Digite novamente.")

