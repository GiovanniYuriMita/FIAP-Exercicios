# FIAP ADS Fase 2, Atividade 1: Exercicio 3 - Simulação de dívidas
# Autor: Giovanni Yuri Mita Chaves, RM 565588
# Data: 29/03/2025

def get_debt_value():
    while True:
        try:
            price = float(input("Informe o valor da dívida: "))
            if price <= 0:
                raise ValueError("O valor deve ser maior que zero.")
            return price
        except ValueError:
            print(f"Entrada inválida. Tente novamente.")

def calculate_prices(debt_value):
    interests = {
        1: 1,
        3: 1.1,
        6: 1.15,
        9: 1.2,
        12: 1.25,
    }

    for i in range (0, len(interests) * 3, 3):
        if i == 0:
            i = 1
        total_price = debt_value * interests[i]
        interests_price = total_price - debt_value
        print(f"\nTotal: R$ {total_price:.2f}\nJuros: R$ {interests_price:.2f}\nNúmero de parcelas: {i}\nValor da parcela: R$ {total_price / i:.2f}")

def calculate_again():
    while True:
        option = input("Deseja calcular outra dívida? (s, n): ")
        if option not in ["s", "n"]:
            print("Opção inválida. Tente novamente.")
            continue
        elif option == "s":
            return True
        return False

def main():
    while True:
        vehicle_price = get_debt_value()
        calculate_prices(vehicle_price)
        if not calculate_again():
            break
    print("Encerrando o programa...")
    

main()