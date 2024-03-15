from abc import ABC, abstractmethod
from datetime import datetime

class Veiculo(ABC):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.preco_por_dia = preco_por_dia

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        pass

    def __str__(self) -> str:
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Preço por dia: R${self.preco_por_dia:.2f}"

class Carro(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias

class Moto(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias

class Caminhao(Veiculo):
    def calcular_aluguel(self, dias: int) -> float:
        return self.preco_por_dia * dias * 1.5 

class SistemaAluguel:
    veiculos_disponiveis = []

    @staticmethod
    def adicionar_veiculo(veiculo: Veiculo):
        SistemaAluguel.veiculos_disponiveis.append(veiculo)

    @staticmethod
    def listar_veiculos_disponiveis():
        for veiculo in SistemaAluguel.veiculos_disponiveis:
            print(veiculo)

    @staticmethod
    def encontrar_veiculos_disponiveis(data: datetime):
        veiculos_disponiveis = []
        for veiculo in SistemaAluguel.veiculos_disponiveis:
            veiculos_disponiveis.append(veiculo)
        return veiculos_disponiveis

def menu():
    print("1. Adicionar veículo")
    print("2. Listar veículos disponíveis")
    print("3. Encontrar veículos disponíveis para aluguel em uma determinada data")
    print("4. Sair")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo_veiculo = input("Digite o tipo de veículo (carro, moto, caminhao): ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            placa = input("Digite a placa do veículo: ")
            preco_por_dia = float(input("Digite o preço de aluguel por dia do veículo: "))

            if tipo_veiculo.lower() == "carro":
                veiculo = Carro(modelo, ano, placa, preco_por_dia)
            elif tipo_veiculo.lower() == "moto":
                veiculo = Moto(modelo, ano, placa, preco_por_dia)
            elif tipo_veiculo.lower() == "caminhao":
                veiculo = Caminhao(modelo, ano, placa, preco_por_dia)
            else:
                print("Tipo de veículo inválido!")
                continue

            SistemaAluguel.adicionar_veiculo(veiculo)
            print("Veículo adicionado com sucesso!")

        elif opcao == "2":
            print("Veículos disponíveis:")
            SistemaAluguel.listar_veiculos_disponiveis()

        elif opcao == "3":
            data = datetime.strptime(input("Digite a data no formato 'dd/mm/aaaa': "), "%d/%m/%Y")
            veiculos_disponiveis = SistemaAluguel.encontrar_veiculos_disponiveis(data)
            print("Veículos disponíveis para aluguel na data especificada:")
            for veiculo in veiculos_disponiveis:
                print(veiculo)

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
