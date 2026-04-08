# Calcula experiencia
#multiplica_por_2(5):
# Debe retornar: [0, 2, 4, 6, 8, 10]

def multiplica_por_2(num):
    lista = []
    for i  in range(num + 1):
        lista.append(i*2)
    return lista
print(multiplica_por_2(5))

# Analiza publicaciones
#suma_y_resta([120, 115])
# Imprime: 235 y retorna: 5

def suma_y_resta(lista):
    print(lista[0]+lista[1])
    return lista[0]- lista[1]
print(suma_y_resta([120, 115]))

# Puntaje ajustado
#sumatoria_menos_longitud([10, 5, 3, 7])
# Suma total = 25, longitud = 4, debe retornar: 21

def sumatoria_menos_longitud(lista):
    total_puntos = 0
    for elemento in lista:
        total_puntos+= elemento
    return total_puntos- len(lista)
print(sumatoria_menos_longitud([10, 5, 3, 7]))


# Ajusta visualizaciones

def valores_multiplicados_segundo(lista):
    if len(lista) >=2:
        lista_nueva=[]
        for elemento in lista:
            lista_nueva.append(elemento*lista[1])
        print(len(lista_nueva))
        return lista_nueva
    else:
        print(len(lista))
        return []


print(valores_multiplicados_segundo([100, 3, 50, 20]))
# Imprime: 4 y retorna: [300, 9, 150, 60]

#valores_multiplicados_segundo([100])
# Imprime: 1 y retorna: []


# Genera precio fijo
#valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

#valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]