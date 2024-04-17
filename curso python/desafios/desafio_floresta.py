# Recebe a quantidade de passos do usuário
quantidade_passos = int(input("Digite a quantidade de passos dados na floresta: "))

# Verifica se a quantidade de passos é positiva
if quantidade_passos > 0:
    # Utiliza um loop for para imprimir a mensagem do explorador
    for passo in range(1, quantidade_passos + 1):
        print(f"Passo {passo}: O explorador caminha pela floresta.")
else:
    # Imprime a mensagem se a quantidade de passos for zero
    print("Nenhum passo dado na floresta.")