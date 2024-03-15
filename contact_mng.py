import json
item_list = {}

def add_item():
        item_name = input("informe o nome do contato: ")
        item_number = int(input("informe o numero do contato: "))
        item_mail = input("informe o e-mail do contato: ")
        item_list[item_name] = (item_number, item_mail)
        
             

def remove_item():
    item_name = input("informe o nome do contato que sera excluido: ")
    del item_list[item_name]

def show_item():
    item_name = input("informe o nome do contato que sera buscado: ")
    x = item_list.get(item_name)
    print(x)

add_item()
add_item()
add_item()
show_item()
remove_item()
show_item()

with open("contacts.json", "w") as file:
    json.dump(item_list, file)