import csv
item_list = {}

def add_item():
        item_name = input("informe o nome do produto: ")
        item_number = int(input("informe o numero do produto: "))
        item_price = int(input("informe o preço do produto: "))
        item_list[item_name] = (item_number, item_price, item_number)
        
             

def remove_item():
    item_name = input("informe o nome do produto que sera excluido: ")
    del item_list[item_name]

def update_item():
    item_name = input("informe o nome do produto que sera alterado: ")
    del item_list[item_name]
    item_name = input("informe o nome do produto: ")
    item_number = int(input("informe o numero do produto: "))
    item_price = input("informe o preço do produto: ")
    item_list[item_name] = (item_number, item_price)
    

add_item()
add_item()
add_item()
update_item()
remove_item()

with open('produtos.csv', 'w', newline='') as arquivo_csv:
    cabecalho = list(item_list.keys())
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
    escritor_csv.writeheader()
    escritor_csv.writerow(item_list)