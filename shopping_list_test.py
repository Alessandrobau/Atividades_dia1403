import shopping_list_test
from shopping_list import *
def test_add_item():
    shopping_list = itens()
    shopping_list.add_item("Produto 1", 10)
    assert "Produto 1" in shopping_list.item_list


def test_remove_item():
    shopping_list = itens()
    shopping_list.add_item("Produto 1", 10)
    shopping_list.remove_item("Produto 1")
    assert "Produto 1" not in shopping_list.item_list


def test_show_items():
    shopping_list = itens()
    shopping_list.add_item("Produto 1", 10)
    shopping_list.add_item("Produto 2", 20)
    shopping_list.show_items()


def test_total_price():
    shopping_list = itens()
    shopping_list.add_item("Produto 1", 10)
    shopping_list.add_item("Produto 2", 20)
    total = shopping_list.total_price()
    assert total == 30


if __name__ == "__main__":
    shopping_list_test.main()
