def executar_selection_sort(lista):
    n = len(lista)
    
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista

lista = [10, 8, 7, 3, 2, 1]
resultado = executar_selection_sort(lista)
print(resultado)
