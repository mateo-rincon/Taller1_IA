from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    #print(f'AAAAAAAAAAAAAAA {state}')
    posActual=state
    posObjetivo=problem.goal
    #print(problem)
    #print(f'Posicion actual: {posActual}, posicion objetivo: {posObjetivo}')
    x1,y1=posActual
    x2,y2=posObjetivo
    mDist=abs(x2-x1)+abs(y2-y1)
    
    return mDist
    utils.raiseNotDefined()


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    x1,y1 = state
    x2,y2 = problem.goal

    A=(x2-x1)**2+(y2-y1)**2
    eucDist=A**(1/2)
    return eucDist
    utils.raiseNotDefined()


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # VERSION INICIAL (sin IA)

    # position, survivors_grid = state
    # survivors = survivors_grid.asList()
    # if not survivors:
    #     return 0
    # x, y = position
    # min_dist = 999999
    # for (sx, sy) in survivors:
    #     d = abs(x - sx) + abs(y - sy)
    #     if d < min_dist:
    #         min_dist = d
    # return min_dist

    # --- PROMPTS USADOS CON IA (resumen) ---
    # - Diseñar una heurística admisible para MultiSurvivorProblem
    #   que considere múltiples sobrevivientes y que sea más informada que solo el más cercano.
    # - Requisito: dejar la primera versión (sin IA) comentada y luego la versión final.
    # - Restricción: no modificar el código de otros problemas, solo survivorHeuristic.

    # VERSIÓN FINAL (con IA): distancia al sobreviviente más cercano
    # + árbol de expansión mínima (MST) sobre los sobrevivientes restantes.
    #
    # Idea:
    # - Si pensamos en el problema como "visitar todos los sobrevivientes", es similar a un
    #   problema tipo TSP en grilla.
    # - Un límite inferior natural del costo óptimo es:
    #     (1) la distancia desde la posición actual al sobreviviente más cercano
    #         +
    #     (2) el costo de conectar todos los sobrevivientes entre sí al menor costo posible,
    #         que podemos aproximar con un árbol de expansión mínima (MST) usando distancias
    #         Manhattan como pesos.
    # - Usar Manhattan como peso mantiene la admisibilidad: el camino real mínimo entre dos
    #   puntos en la grilla (considerando paredes y terrenos costosos) nunca será menor que
    #   su distancia Manhattan en pasos, y cada paso cuesta al menos 1.

    position, survivors_grid = state
    survivors = survivors_grid.asList()

    # Si no quedan sobrevivientes, el costo restante es 0.
    if not survivors:
        return 0

    # Distancia Manhattan entre dos posiciones.
    def manhattan(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    # (1) Distancia desde la posición actual al sobreviviente más cercano.
    min_to_survivor = min(manhattan(position, s) for s in survivors)

    # (2) Costo de un MST sobre los sobrevivientes restantes usando distancias Manhattan.
    #
    # Implementamos Prim sobre la lista de sobrevivientes. Usar solo sobrevivientes (y no
    # incluir la posición actual) evita contar dos veces el tramo inicial.
    if len(survivors) == 1:
        mst_cost = 0
    else:
        # Para poder usar conjuntos, trabajamos con tuplas (que ya lo son).
        remaining = list(survivors)
        connected = {remaining[0]}
        not_connected = set(remaining[1:])
        mst_cost = 0

        while not_connected:
            best_dist = float("inf")
            best_point = None

            for p in connected:
                for q in not_connected:
                    d = manhattan(p, q)
                    if d < best_dist:
                        best_dist = d
                        best_point = q

            mst_cost += best_dist
            connected.add(best_point)
            not_connected.remove(best_point)

    # Heurística total: parte inicial + MST entre sobrevivientes.
    # Esto es un subestimador del costo real mínimo para rescatar a todos.
    return min_to_survivor + mst_cost