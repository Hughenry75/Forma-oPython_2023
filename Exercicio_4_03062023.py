# Formula para calculo da área do retângulo (multiplicando o comprimento pela largura)
def calcula_area_retangulo(comprimento, largura):
    area_retangulo = comprimento * largura
    return area_retangulo

# Aqui é pedida a medida do rectangulo
comprimento = float(input("Qual o comprimento do retângulo: "))
largura = float(input("Qual a largura do retângulo: "))

area_retangulo = calcula_area_retangulo(comprimento, largura)

# Imprimir a área do retângulo
print(f"A área do retângulo é: {area_retangulo} cm²")