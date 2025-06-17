class No:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def remover_filho(self, nome_filho):
        self.filhos = [f for f in self.filhos if f.nome != nome_filho]

    def mostrar(self, nivel=0):
        print("  " * nivel + "- " + self.nome)
        for filho in self.filhos:
            filho.mostrar(nivel + 1)

    def buscar(self, nome):
        if self.nome.lower() == nome.lower():
            return self
        for filho in self.filhos:
            encontrado = filho.buscar(nome)
            if encontrado:
                return encontrado
        return None


def menu():
    print("\n--- Menu da Fazenda ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar estrutura da fazenda")
    print("4. Buscar item")
    print("5. Sair")


# Criando estrutura base
raiz = No("Fazenda")
animais = No("Animais")
plantacoes = No("Plantações")
trabalhadores = No("Trabalhadores")

raiz.adicionar_filho(animais)
raiz.adicionar_filho(plantacoes)
raiz.adicionar_filho(trabalhadores)

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        setor = input("Adicionar em qual setor (Animais, Plantações, Trabalhadores)? ").capitalize()
        nome_item = input("Nome do item: ")
        setor_encontrado = raiz.buscar(setor)
        if setor_encontrado:
            setor_encontrado.adicionar_filho(No(nome_item))
            print(f"{nome_item} adicionado ao setor {setor}.")
        else:
            print("Setor não encontrado.")

    elif escolha == "2":
        nome_item = input("Nome do item a remover: ")
        for setor in raiz.filhos:
            setor.remover_filho(nome_item)
        print(f"{nome_item} removido, se existia.")

    elif escolha == "3":
        print("\n--- Estrutura da Fazenda ---")
        raiz.mostrar()

    elif escolha == "4":
        nome_item = input("Nome do item para buscar: ")
        encontrado = raiz.buscar(nome_item)
        if encontrado:
            print(f"{nome_item} foi encontrado na fazenda!")
        else:
            print(f"{nome_item} não encontrado.")

    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
