
#Gerar uma lista de quadrados dos números de 0 a 9:
squares = [x ** 2 for x in range(10)]
print(squares)

#Filtrar números pares de uma lista:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#Converter uma lista de strings para maiúsculas:
words = ['apple', 'banana', 'cherry', 'date']
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

#Criar uma lista de tuplas com elementos de duas listas:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(x, y) for x in list1 for y in list2]
print(combined_list)

#Filtrar e modificar elementos de uma lista:
grades = [85, 90, 78, 95, 88]
adjusted_grades = [grade + 5 if grade >= 90 else grade for grade in grades]
print(adjusted_grades)

#Criar uma lista de palavras com mais de três letras:
sentence = "This is a sample sentence with some words."
words = sentence.split()
long_words = [word for word in words if len(word) > 3]
print(long_words)

#Gerar uma lista de números primos:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in range(2, 50) if is_prime(x)]
print(prime_numbers)

#Criar uma lista de valores booleanos indicando se os números são pares:
numbers = [2, 5, 8, 11, 14]
is_even = [num % 2 == 0 for num in numbers]
print(is_even)

#Gerar uma lista de listas representando uma matriz:
matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print(matrix)

#Filtrar elementos únicos de uma lista:
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)