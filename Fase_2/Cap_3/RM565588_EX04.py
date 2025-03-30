# FIAP ADS Fase 2, Atividade 1: Exercicio 4 - Simulação de resgate de ações
# Autor: Giovanni Yuri Mita Chaves, RM 565588
# Data: 29/03/2025

def input_loop(valid_values, type, prompt, error_message):
    while True:
        try:
            value = type(input(prompt))

            if isinstance(valid_values, list):
                if value not in valid_values:
                    print(error_message)
                    continue
                return value
            else:
                if value <= valid_values:
                    print(error_message)
                    continue
                return value
        except ValueError:
            print(f"Entrada inválida. Tente novamente.")

def get_investment():
    print("Escolha o tipo de investimento:\n1. CDB\n2. LCI\n3. LCA\n")

    investment = input_loop(
        [1, 2, 3],
        int,
        "Digite o tipo de investimento (1, 2 ou 3): ",
        "Selecione uma opção válida."
    )

    return investment

def get_money_to_reclaim():
    price = input_loop(
        0,
        float,
        "Digite o valor a ser resgatado: ",
        "O valor deve ser maior que zero."
    )
    
    return price

def get_applied_days():
    applied_days = input_loop(
        0, 
        int, 
        "Digite o número de dias que o valor permaneceu investido: ", 
        "O valor deve ser maior que zero."
    )
    
    return applied_days

def calculate_income_tax(investment, money_to_reclaim, applied_days):
    if applied_days <= 180:
        tax = 0.225
    elif applied_days <= 360:
        tax = 0.2
    elif applied_days <= 720:
        tax = 0.175
    else:
        tax = 0.15

    income_tax = money_to_reclaim * tax
    print(f"O valor do Imposto de Renda a ser pago é: R$ {income_tax:.2f}")

def simulate_again():
    sa = input_loop(
        ["s", "n"],
        str,
        "Deseja simular outro resgate? (s, n): ",
        "Opção inválida. Tente novamente."
    )

    if sa == "s":
        return True
    return False

def main():
    print("Simulador de resgate de ações")
    while True:
        investment_name = get_investment()
        if investment_name != 1:
            print("Não há imposto de renda para LCI e LCA.")
        else:
            money_to_reclaim = get_money_to_reclaim()
            applied_days = get_applied_days()

            calculate_income_tax(investment_name, money_to_reclaim, applied_days)

        if not simulate_again():
            break
    print("Encerrando o programa...")

main()