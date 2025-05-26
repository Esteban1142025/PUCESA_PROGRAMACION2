#


#dollars = [1.3, 14.7, 19.8, 8.1, 18.9, 3.4, 15.6, 16.3, 9.4, 17.2]
dollars = [3.4, 1.3, 8.1, 9.4, 14.7, 15.6, 16.3, 17.2, 18.9, 19.8]

comp_bs = 0
inter_bs = 0

comp_is = 0
inter_is = 0

comp_ss = 0
inter_ss = 0

def bubble_sort(dollars):
    n = len(dollars)
    global comp_bs, inter_bs

    for i in range(n):
        comp_bs += 1
        for j in range(0, n - i - 1):
            if dollars[j] > dollars[j + 1]:
                inter_bs += 1
                dollars[j], dollars[j + 1] = dollars[j + 1], dollars[j]
    return dollars

print("Original:", dollars)
print("Ordenado:", bubble_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_bs)
print("Numero de intercambios realizados: ",inter_bs)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def insertion_sort(dollars):
    global comp_is, inter_is

    for i in range(0, len(dollars)):
        comp_is += 1
        actual = dollars[i]
        j = i - 1
        while j >= 0 and dollars[j] > actual:
            inter_is += 1
            dollars[j + 1] = dollars[j]
            j -= 1
        dollars[j + 1] = actual
    return dollars

print("Original:", dollars)
print("Ordenado:", insertion_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_is)
print("Numero de intercambios realizados: ",inter_is)
print("\n")

#/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def selection_sort(dollars):
    n = len(dollars)
    global comp_ss, inter_ss
    
    for i in range(n):
        comp_ss += 1
        minimo = i
        for j in range(i + 1, n):
            if dollars[j] < dollars[minimo]:
                inter_ss += 1
                minimo = j 
        if minimo != i:
            inter_ss += 1
            dollars[i], dollars[minimo] = dollars[minimo], dollars[i]

    return dollars

print("Original:", dollars)
print("Ordenado:", selection_sort(dollars.copy()))
print("Numero de comparaciones realizadas: ",comp_ss)
print("Numero de intercambios realizados: ",inter_ss)
