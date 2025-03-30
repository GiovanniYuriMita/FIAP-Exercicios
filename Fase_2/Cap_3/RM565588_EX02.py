# FIAP ADS Fase 2, Atividade 1: Exercicio 2 - Compra de veículo
# Autor: Giovanni Yuri Mita Chaves, RM 565588
# Data: 29/03/2025
# Material consultado para referência:

def get_vehicle_price():
    while True:
        try:
            price = float(input("Informe o preço do veículo: "))
            if price <= 0:
                raise ValueError("O preço deve ser maior que zero.")
            return price
        except ValueError:
            print(f"Entrada inválida. Tente novamente.")

def calculate_prices(vehicle_price):
    installments = {
        6: 1.03,
        12: 1.06,
        18: 1.09,
        24: 1.12,
        30: 1.15,
        36: 1.18,
        42: 1.21,
        48: 1.24,
        54: 1.27,
        60: 1.3
    }

    total_price = vehicle_price * 0.8
    print(f"O preço final à vista com desconto de 20% é R$ {total_price:.2f}")
    for i in range (6, len(installments) * 6 + 1, 6):
        total_price = vehicle_price * installments[i]
        installments_price = vehicle_price * installments[i] / i
        print(f"O preço final parcelado em {i}x é de R$ {total_price:.2f}, com parcelas de R$ {installments_price:.2f}")

def calculate_again():
    while True:
        option = input("Deseja calcular novamente? (s, n): ")
        if option not in ["s", "n"]:
            print("Opção inválida. Tente novamente.")
            continue
        elif option == "s":
            return True
        return False

def main():
    while True:
        vehicle_price = get_vehicle_price()
        calculate_prices(vehicle_price)
        if not calculate_again():
            break
    print("Encerrando o programa...")
    

main()