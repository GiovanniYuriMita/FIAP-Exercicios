# FIAP ADS Fase 2, Atividade 1: Exercicio 1 - Votação de dia da semana na Fintech Bidu
# Autor: Giovanni Yuri Mita Chaves, RM 565588
# Data: 29/03/2025
# Material consultado para referência:
# https://www.geeksforgeeks.org/input-validation-in-python/
# https://realpython.com/sort-python-dictionary/#:~:text=To%20sort%20a%20dictionary%20by,function%20to%20extract%20the%20value.&text=Yes%2C%20you%20can%20sort%20a,to%20the%20sorted()%20function.

def meeting_voting():
    valid_weekdays = [
        "segunda-feira", 
        "terça-feira", 
        "quarta-feira", 
        "quinta-feira",
        "sexta-feira"
    ]

    voted_weekdays = { day: 0 for day in valid_weekdays }

    while True:
        try:
            pnumber = int(input("Informe o número de colaboradores: "))

        except ValueError:
            print("Por favor, insira um número inteiro.")
            continue
        if pnumber <= 1:
            print("O número de colaboradores deve ser maior que 1.")
            continue
        break
        

    for i in range(int(pnumber)):
        while True:
            preferred_day = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira ou sexta-feira): ").lower()
            
            if preferred_day in valid_weekdays:
                voted_weekdays[preferred_day] += 1
                print(f"*O colaborador {i+1} votou no dia {preferred_day}.")
                break
            print("Dia da semana inválido. Tente novamente")

    return voted_weekdays

def display_votes(sorted_voted_weekdays):
    for day in range(len(sorted_voted_weekdays)):
        print(f"{sorted_voted_weekdays[day][0]}: {sorted_voted_weekdays[day][1]} voto(s)")

def handle_votes(voted_weekdays):
    sorted_voted_weekdays = sorted(voted_weekdays.items(), key=lambda item: item[1], reverse=True)

    if sorted_voted_weekdays[0][1] == sorted_voted_weekdays[1][1]:
        print(f"Houve um empate:")
        display_votes(sorted_voted_weekdays)
        while True:
            vote_again = input("Deseja votar novamente? (s/n): ").lower()
            if vote_again not in ['s', 'n']:
                print("Opção inválida. Tente novamente.")
                continue
            elif vote_again == 's':
                return True
            else:
                print("Finalizando o programa...")
                return False
    else:
        print(f"O dia {sorted_voted_weekdays[0][0]} foi escolhido com {sorted_voted_weekdays[0][1]} voto(s).")
        display_votes(sorted_voted_weekdays)
        return False

def main():
    while True:
        print("--- Sistema de votação de dia da semana ---")
        voted_weekdays = meeting_voting()
        if not handle_votes(voted_weekdays):
            break
    print("Votação encerrada.")

main()