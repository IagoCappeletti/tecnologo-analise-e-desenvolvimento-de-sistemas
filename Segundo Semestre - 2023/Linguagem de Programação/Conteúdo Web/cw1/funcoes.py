def imprimir_mensagem(diciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na diciplina: {diciplina}, do curso: {curso}.")

imprimir_mensagem("Python", "ADS")
imprimir_mensagem("Java", "ADS")

###################################

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def diminuir(a, b):
    return a * b

def dividir(a, b):
    return a / b

soma = somar(2, 4)
print(soma)

soma = diminuir(24, 2)
print(soma)

soma = diminuir(2, 4)
print(soma)

divide = dividir(4, 2)
print(divide)

###################################

def calcular_desconto(valor, desconto=0):
    #O parâmetro desconto possui zero com valor default
    valor_com_desconto = valor - (valor *desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #Não passando nenhum desconto
valor2 = calcular_desconto(100, 0.25) #Passando 25% de desconto

print(f"\Primeiro valor a ser pago = {valor1}")
print(f"\Segundo valor a ser pago = {valor2}")

###################################

def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_maiuscula(texto="Friend", flag_maiuscula=True)
print(texto)

###################################

def converter_maiuscula(texto, flag_maiuscula = True): #O parâmetro flag_minuscula possui True como valor default
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto1 = converter_maiuscula(texto="Linguagem de Programação", flag_maiuscula = True)
texto2 = converter_maiuscula(texto="Is he your friend?")

print(f"Texto 1 = {texto1}")
print(f"Texto 2 = {texto2}")

###################################

def imprimir_parametros(*args):
    quantidade_paremetros = len(args)
    print(f"Quantidade de parâmetros = {quantidade_paremetros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1 ")
imprimir_parametros("São Paulo", 10, 23.75, "João")
print("\nChamada 2 ")
imprimir_parametros("São Paulo")

###################################

def imprime_parametros(**kwargs):
    print(f"tipo de objeto recebido = {type(kwargs)}\n")
    quantidade_parametros = len(kwargs)
    print(f"quantidade de parâmetros = {quantidade_parametros}")

    for chave, valor in kwargs.items():
        print(f"Varíavel = {chave}, valor = {valor}")

print("\nChamada 1 ")
imprime_parametros(cidade = "São Paulo", idade = 10, nome = "João")
print("\nChamada 2 ")
imprime_parametros(desconto = 10, valor = 100)