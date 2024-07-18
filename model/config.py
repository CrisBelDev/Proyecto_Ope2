import numpy as np

def capturar_datos(matriz):
    min_values = np.min(matriz, axis=1)
    max_values = np.max(matriz, axis=0)
    
    max_of_mins = np.max(min_values)
    min_of_maxs = np.min(max_values)
    
    estrategia = 'estrategia pura' if max_of_mins == min_of_maxs else 'estrategia mixta'
    
    return matriz, min_values, max_values, max_of_mins, min_of_maxs, estrategia

def calcular_estrategias_mixtas(matriz):
    a, b = matriz[0]
    c, d = matriz[1]
    
    q = (d - b) / (a - b - c + d)
    p = (d - c) / (a - c - b + d)
    
    return p, q

# Ejemplo de uso
matriz = np.array([[1, 6], [15, 0]])

matriz, min_values, max_values, max_of_mins, min_of_maxs, estrategia = capturar_datos(matriz)

print("Matriz de datos:")
print(matriz)
print("Mínimos de cada fila:", min_values)
print("Máximos de cada columna:", max_values)
print("Mayor de los mínimos:", max_of_mins)
print("Menor de los máximos:", min_of_maxs)
print("Tipo de estrategia:", estrategia)

if estrategia == 'estrategia mixta':
    p, q = calcular_estrategias_mixtas(matriz)
    print(f"Probabilidades calculadas: p = {p:.2f}, q = {q:.2f}")




def calcular_equilibrio(CC1, CC2, CM1, CM2, MC1, MC2, MM1, MM2):
    mensaje = "Equilibrios de Nash encontrados:\n"

    # Verificar equilibrios de Nash
    # Confesar-Confesar
    if CC1 >= MC1 and CC2 >= CM2:
        mensaje += f"Confesar-Confesar ({CC1}, {CC2})\n"
    # Confesar-Mentir
    if CM1 >= MM1 and CM2 >= CC2:
        mensaje += f"Confesar-Mentir ({CM1}, {CM2})\n"
    # Mentir-Confesar
    if MC1 >= CC1 and MC2 >= MM2:
        mensaje += f"Mentir-Confesar ({MC1}, {MC2})\n"
    # Mentir-Mentir
    if MM1 >= CM1 and MM2 >= MC2:
        mensaje += f"Mentir-Mentir ({MM1}, {MM2})\n"

    # Si no se encuentra ningún equilibrio, ajustar mensaje
    if mensaje == "Equilibrios de Nash encontrados:\n":
        mensaje = "No se encontraron equilibrios de Nash."

    mensaje += '\nEl dilema muestra que, aunque la mejor opción conjunta sería cooperar (1 año de prisión cada uno), la estrategia dominante para ambos es traicionar, ya que minimiza el peor resultado posible individualmente.\nEn términos de teoría de juegos, la traición es el equilibrio de Nash, ya que ninguna de las partes mejora su situación al cambiar su estrategia, dado que el otro también está traicionando.\nPor lo tanto, ambos terminan recibiendo 3 años de prisión.'

    return mensaje

# Ejemplo de uso
CC1 = 3
CC2 = 3
CM1 = 0
CM2 = 6
MC1 = 6
MC2 = 0
MM1 = 1
MM2 = 1

resultado = calcular_equilibrio(CC1, CC2, CM1, CM2, MC1, MC2, MM1, MM2)
print(resultado)
