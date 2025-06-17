class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child_name):
        self.children = [c for c in self.children if c.name != child_name]

    def show(self, level=0):
        print("  " * level + "- " + self.name)
        for child in self.children:
            child.show(level + 1)

    def search(self, name):
        if self.name.lower() == name.lower():
            return self
        for child in self.children:
            found = child.search(name)
            if found:
                return found
        return None


def menu():
    print("\n--- Menu da Fazenda ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar estrutura da fazenda")
    print("4. Buscar item")
    print("5. Sair")


# Creating base structure
root = Node("Fazenda")
animals = Node("Animais")
crops = Node("Plantações")
workers = Node("Trabalhadores")

root.add_child(animals)
root.add_child(crops)
root.add_child(workers)

while True:
    menu()
    choice = input("Escolha uma opção: ")

    if choice == "1":
        sector = input("Adicionar em qual setor (Animais, Plantações, Trabalhadores)? ").capitalize()
        item_name = input("Nome do item: ")
        found_sector = root.search(sector)
        if found_sector:
            found_sector.add_child(Node(item_name))
            print(f"{item_name} adicionado ao setor {sector}.")
        else:
            print("Setor não encontrado.")

    elif choice == "2":
        item_name = input("Nome do item a remover: ")
        for sector in root.children:
            sector.remove_child(item_name)
        print(f"{item_name} removido, se existia.")

    elif choice == "3":
        print("\n--- Estrutura da Fazenda ---")
        root.show()

    elif choice == "4":
        item_name = input("Nome do item para buscar: ")
        found = root.search(item_name)
        if found:
            print(f"{item_name} foi encontrado na fazenda!")
        else:
            print(f"{item_name} não encontrado.")

    elif choice == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
