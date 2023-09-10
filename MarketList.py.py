# Dicionário para armazenar as listas de itens
menu = {
    "frutas": [],
    "grãos": [],
    "carnes": []
}

# Função para mostrar o menu
def mostrar_menu():
    print("Escolha um menu:")
    print("1. Frutas")
    print("2. Grãos")
    print("3. Carnes")
    print("4. Sair")

# Função para adicionar item a uma lista
def adicionar_item(menu, categoria):
    item = input(f"Digite o {categoria} que deseja adicionar: ")
    menu[categoria].append(item)

# Inicializar uma variável para controlar o loop
continuar = True

while continuar:
    # Mostrar o menu principal
    mostrar_menu()

    # Solicitar a escolha do usuário
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        # Acessar o menu de frutas
        while True:
            print("\nMenu de Frutas:")
            for i, item in enumerate(menu["frutas"], start=1):
                print(f"{i}. {item}")

            print("Ações:")
            print("1. Adicionar uma fruta")
            print("2. Voltar ao menu principal")
            sub_escolha = input("Digite o número da ação desejada: ")

            if sub_escolha == "1":
                adicionar_item(menu, "frutas")
            elif sub_escolha == "2":
                break
            else:
                print("Opção inválida.")

    elif escolha == "2":
        # Acessar o menu de grãos
        while True:
            print("\nMenu de Grãos:")
            for i, item in enumerate(menu["grãos"], start=1):
                print(f"{i}. {item}")

            print("Ações:")
            print("1. Adicionar um grão")
            print("2. Voltar ao menu principal")
            sub_escolha = input("Digite o número da ação desejada: ")

            if sub_escolha == "1":
                adicionar_item(menu, "grãos")
            elif sub_escolha == "2":
                break
            else:
                print("Opção inválida.")

    elif escolha == "3":
        # Acessar o menu de carnes
        while True:
            print("\nMenu de Carnes:")
            for i, item in enumerate(menu["carnes"], start=1):
                print(f"{i}. {item}")

            print("Ações:")
            print("1. Adicionar uma carne")
            print("2. Voltar ao menu principal")
            sub_escolha = input("Digite o número da ação desejada: ")

            if sub_escolha == "1":
                adicionar_item(menu, "carnes")
            elif sub_escolha == "2":
                break
            else:
                print("Opção inválida.")

    elif escolha == "4":
        # Sair do programa
        continuar = False

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("Programa encerrado.")