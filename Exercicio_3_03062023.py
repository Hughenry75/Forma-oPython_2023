
numeros = []

for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

print("Números pares:")

for num in numeros:
    if num % 2 == 0:
        print(num)
