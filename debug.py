
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",  # Altere para sua senha real
    database="school_universe"
)
cursor = conn.cursor()

#adicionar_cliente
def adicionar_cliente():
    while True:
        
         # Validar nome (obrigatório)
        nome = input("Nome do Cliente: ").strip() # retira espaços no fim e no começo da variavel
        if nome:
            break
        print("O nome é obrigatório. Por favor, digite.")

         #Validar CPF (obrigatório)
    while True:
        cpf = input("CPF do Cliente (11 dígitos): ").strip()
        if len(cpf) == 11 and cpf.isdigit(): # verifica se tem 11 digitos e se sao numericos de 0-9
            break
        print("CPF inválido! Digite exatamente 11 dígitos numéricos.")
        
         #Validar Data de nascimeto (obrigatório)
    while True:
        data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(data_nascimento, "%Y-%m-%d")
            break
        except ValueError:
            print("Data inválida! Use o formato YYYY-MM-DD, exemplo: 2007-03-31.")

    rg = input("RG do Cliente (opcional): ").strip()
    numero_telefone = input("Número de Telefone (opcional): ").strip()
    email = input("Email (opcional): ").strip()
    estado = input("Estado (opcional): ").strip()
    cidade = input("Cidade (opcional): ").strip()
    rua = input("Rua (opcional): ").strip()
    cep = input("CEP (opcional): ").strip()
    bairro = input("Bairro (opcional): ").strip()
    complemento = input("Complemento (opcional): ").strip()

    cursor.execute("""
        INSERT INTO Clientes (
            nome, cpf, data_nascimento, rg, numero_telefone, email, estado,
            cidade, rua, cep, bairro, complemento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (nome, cpf, data_nascimento, rg, numero_telefone, email, estado,
          cidade, rua, cep, bairro, complemento))
    conn.commit() # atualiza o BD e salva

    cursor.execute("SELECT LAST_INSERT_ID()") # retorna o ultimo id inserido
    cliente_id = cursor.fetchone()[0]

    cursor.execute("SELECT id_produto FROM Produto ORDER BY RAND() LIMIT 1") #retirna um ID aleatorio da tabela Produto e coloca na variavel produto
    produto = cursor.fetchone() # separa a linha retornada e separa em ordem  para ser tratada como lista

    if produto:
        produto_id = produto[0] # o produto 0 é sempre o ID do produto
        cursor.execute("""
            UPDATE Produto
            SET cliente_id = %s
            WHERE id_produto = %s
        """, (cliente_id, produto_id))
        conn.commit()
        print(f"Cliente {nome} cadastrado com sucesso e associado ao produto ID {produto_id}.")
    else:
        print(f"Cliente {nome} cadastrado com sucesso, mas não há produtos disponíveis.")

#editar
def editar_cliente():
    id_cliente = input("Digite o ID do cliente para editar: ").strip() # Strip retira os espaços no começo e no fim das variaveis
    if not id_cliente.isdigit(): # retora verdadeiro caso nao tenha nenhum cliente com id selecionado
        print("ID inválido.")
        return
    id_cliente = int(id_cliente)

    cursor.execute("SELECT * FROM Clientes WHERE id_clientes = %s", (id_cliente,)) # seleciona para alteração alinha da tabela com o ID da variavel
    if not cursor.fetchone(): # verifica se o id da variavel esta presente na tabela
        print("Cliente não encontrado.")
        return

    # Validar nome (obrigatório)
    while True:
        novo_nome = input("Novo nome: ").strip()
        if novo_nome:
            break
        print("O nome é obrigatório. Por favor, digite.")

    # Validar CPF (obrigatório, 11 dígitos numéricos)
    while True:
        novo_cpf = input("Novo CPF (11 dígitos): ").strip()
        if len(novo_cpf) == 11 and novo_cpf.isdigit(): # verifica se tem 11 digitos e sao numericos de 0-9
            break
        print("CPF inválido! Digite exatamente 11 dígitos numéricos.")

    # Validar data de nascimento (obrigatório)
    while True:
        nova_data_nascimento = input("Nova data de nascimento (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(nova_data_nascimento, "%Y-%m-%d") # tenta deixar em formato de ano-mes-dia (formato americano)
            break
        except ValueError:
            print(" Data inválida! Use o formato YYYY-MM-DD, exemplo: 2007-03-31.") # caso nao esteja no formato correto retorna erro

    cursor.execute("""
        UPDATE Clientes
        SET nome = %s, cpf = %s, data_nascimento = %s
        WHERE id_clientes = %s
    """, (novo_nome, novo_cpf, nova_data_nascimento, id_cliente))
    conn.commit()
    print("Cliente atualizado com sucesso.")

#apagar
def apagar_cliente():
    id_cliente = input("Digite o ID do cliente para apagar: ").strip()
    if not id_cliente.isdigit(): #apenas numeros 0-9
        print("ID inválido.")
        return
    id_cliente = int(id_cliente)

    cursor.execute("SELECT * FROM Clientes WHERE id_clientes = %s", (id_cliente,))
    if not cursor.fetchone(): #caso nao ache o ID em nenhuma linha
        print("Cliente não encontrado.")
        return

    cursor.execute("UPDATE Produto SET cliente_id = NULL WHERE cliente_id = %s", (id_cliente,)) # apaga o id_Cliente da tabela produto
    cursor.execute("DELETE FROM Clientes WHERE id_clientes = %s", (id_cliente,)) # apaga o cliente da tabela
    conn.commit() # salva alterações no BD
    print("Cliente apagado com sucesso.")

#listar
def listar_clientes():
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall() # separa a linha da tabela em uma lista 
    if clientes:
        for cliente in clientes:
            print("\n--- Cliente ID:", cliente[0], "---")
            print(f"Nome: {cliente[1]}") # obrigatorio
            print(f"CPF: {cliente[2]}") # obrtigatorio
            print(f"RG: {cliente[3] if cliente[3] else '-'}")
            print(f"Data de Nascimento: {cliente[4]}") # obrigatorio
            print(f"Telefone: {cliente[5] if cliente[5] else '-'}")
            print(f"Email: {cliente[6] if cliente[6] else '-'}")
            print(f"Estado: {cliente[7] if cliente[7] else '-'}")
            print(f"Cidade: {cliente[8] if cliente[8] else '-'}")
            print(f"Rua: {cliente[9] if cliente[9] else '-'}")
            print(f"CEP: {cliente[10] if cliente[10] else '-'}")
            print(f"Bairro: {cliente[11] if cliente[11] else '-'}")
            print(f"Complemento: {cliente[12] if cliente[12] else '-'}")
            print(f"Criado em: {cliente[13]}")
    else:
        print("Nenhum cliente encontrado.")

#menu
def menu():
    while True:
        print("\n____________________________________")
        print("1- Listar Clientes")
        print("2- Adicionar Cliente")
        print("3- Editar Cliente")
        print("4- Apagar Cliente")
        print("5- Sair")
        print("____________________________________")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_clientes()
        elif opcao == '2':
            adicionar_cliente()
        elif opcao == '3':
            editar_cliente()
        elif opcao == '4':
            apagar_cliente()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
                
cursor.close()
conn.close()
