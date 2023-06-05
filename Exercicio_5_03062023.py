# inverter a ordem dos caracteres de um nome.
def inverter_nome(nome):
    nome_invertido = nome[::-1]  # Utiliza o slice com passo -1 para inverter a ordem dos caracteres
    return nome_invertido

nome_completo = input("Digite seu nome completo: ")
nome_invertido = inverter_nome(nome_completo)
print("Nome invertido:", nome_invertido)