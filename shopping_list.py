class itens:
    def __init__(self):
        self.item_list = {}

    def add_item(self):
        item_name = input("informe o nome do produto: ")
        item_price = int(input("informe o preço do produto: "))
        self.item_list[item_name] = item_price

    def remove_item(self):
        item_name = input("informe o nome do item: ")
        del self.item_list[item_name]

    def show_item(self):
        print(self.item_list)

    def total_price(self):
        newValue = {}
        newValue = {sum(self.item_list.values())}
        print(newValue)

shopping_list = itens()
shopping_list.add_item()
shopping_list.add_item()
shopping_list.show_item()
shopping_list.remove_item()
shopping_list.show_item()
shopping_list.total_price()


