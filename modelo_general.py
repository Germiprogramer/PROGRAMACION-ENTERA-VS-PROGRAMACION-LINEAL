# Importar OR-Tools para programación lineal
from ortools.linear_solver import pywraplp

UNIDADES3 = [
    'Espadachines',
    'Hombres de armas',
    'Arqueros',
    'Ballesteros',
    'Arcabuceros',
    'Jinetes',
    'Caballeros',
    'Arietes',
    'Catapultas',
    'Mangonelas',]

DATOS3 = [
    [60, 20, 0, 6, 70],
    [100, 0, 20, 12, 155],
    [30, 50, 0, 5, 70],
    [80, 0, 40, 12, 80],
    [120, 0, 120, 35, 150],
    [100, 20, 0, 9, 125],
    [140, 0, 100, 24, 230],
    [0, 300, 0, 200, 700],
    [0, 250, 250, 30, 200],
    [0, 400, 200, 12*3, 240]]

RECURSOS3 = [183000, 90512, 80150]

def resolver_ejercito3(UNIDADES, DATOS, RECURSOS):
    # Crear el solucionador lineal utilizando el backend CBC
    solucionador = pywraplp.Solver('Maximizar poder del ejército', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    
    # 1. Crear las variables que queremos optimizar
    unidades = [solucionador.IntVar(0, solucionador.infinity(), unidad) for unidad in UNIDADES]
    
    # 2. Agregar restricciones para cada recurso
    for r, _ in enumerate(RECURSOS):
        solucionador.Add(sum(DATOS[u][r] * unidades[u] for u, _ in enumerate(unidades)) <= RECURSOS[r])
    
    # 3. Maximizar la nueva función objetivo
    solucionador.Maximize(sum((10*DATOS[u][-2] + DATOS[u][-1]) * unidades[u] for u, _ in enumerate(unidades)))
    
    # Resolver el problema
    estado = solucionador.Solve()
    
    # Si se ha encontrado una solución óptima, imprimir los resultados
    if estado == pywraplp.Solver.OPTIMAL:
        print('================= Solución =================')
        print(f'Resuelto en {solucionador.wall_time():.2f} milisegundos en {solucionador.iterations()} iteraciones')
        print()
        print(f'Valor óptimo = {solucionador.Objective().Value()} 💪poder')
        print('Ejército:')
        for u, _ in enumerate(unidades):
            print(f' - {unidades[u].name()} = {unidades[u].solution_value()}')
    else:
        print('El solucionador no pudo encontrar una solución óptima.')


