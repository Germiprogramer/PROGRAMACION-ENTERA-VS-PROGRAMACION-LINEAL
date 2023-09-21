# MIP

# Importar OR-Tools para programación lineal

from ortools.linear_solver import pywraplp

# establecer los datos

UNIDADES1 = ["Espadachines", "Arqueros", "Caballeros"]

DATOS1 = [[60, 20, 0, 70],        
        [80, 10, 40, 95],
        [140, 0, 100, 230]]

RECURSOS1 = [1200, 800, 600]

def resolver_ejercito1(UNIDADES, DATOS, RECURSOS):
    # Create the linear solver using the CBC backend
    solver = pywraplp.Solver('Maximizar el poder de la armada', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
  
    # Definir las variables
    unidades = [solver.IntVar(0, solver.infinity(), unidad) for unidad in UNIDADES]

    # Definir las restricciones
    for r, _ in enumerate(RECURSOS):
        solver.Add(sum(DATOS[u][r] * unidades[u] for u, _ in enumerate(unidades)) <= RECURSOS[r])
    # Definir la función objetivo
    solver.Maximize(sum(DATOS[u][-1] * unidades[u] for u, _ in enumerate(unidades)))

    # Resolver el sistema
    status = solver.Solve()

    # Imprimir la solución

    if status == pywraplp.Solver.OPTIMAL:
        print('Solución:')
        print('Valor objetivo =', solver.Objective().Value())
        for u, _ in enumerate(unidades):
            print(unidades[u].name(), '=', unidades[u].solution_value())
    else:
        print('El problema no tiene solución óptima.')