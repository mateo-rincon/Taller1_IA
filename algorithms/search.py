from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # TODO: Add your code here
    """camino = []
    visitados=[]
    stack= utils.Stack()
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    inicio= problem.getSuccessors(problem.getStartState())

    estadoActual=problem.getStartState()

    for i in inicio:
        stack.push(i)
        #print(estado)
    
    while problem.isGoalState(estadoActual[0])==False:
        
        estadoActual=stack.pop()
        if problem.isGoalState(estadoActual[0]):
            print('LLEGUE')
            
        else:
            #print(f'AAAAAA: {estadoActual}')
            for i in problem.getSuccessors(estadoActual[0]):
                #print(f'AAAAA: {i}')
                if i not in visitados:
                    stack.push(i)
                    visitados.append(i)
    
    
    """#PROMPT: El codigo original hecho a mano
    stack = utils.Stack()
    visited = set()

    # Cada elemento del stack será: (estado, lista_de_acciones)
    start_state = problem.getStartState()
    stack.push((start_state, []))

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                new_actions = actions + [action]
                stack.push((successor, new_actions))

    return []

    
        
    #print(f"el stack es {stack}")

    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    #PROMPT: considerando el taller que te subi anteriormente, cree el siguiente codigo de BFS. Ayudame a modificarlo para cumplir con el enunciado.
    """def breadthFirstSearch(problem: SearchProblem):
    fila = utils.Queue()
    visited = set()
    start_state= problem.getStartState()
    fila.push((start_state, []))
    actions = []
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    while not fila.isEmpty():
        state, actions = fila.pop()
        
        posibleObjetivo = problem.isGoalState(state)
        if posibleObjetivo == True:
            return actions
            print("llegué")
        
        else:
            if state not in visited:
                visited.add(state)
        
            sucesores = problem.getSuccessors(state)
            for successor, action, cost in sucesores:
                if successor not in visited:
                    visited.add(successor)
                    actions = actions + action
                    fila.push((successor, actions))
                    
    return []
    """
    
    # TODO: Add your code here
    fila = utils.Queue()
    visited = set()
    start_state = problem.getStartState()
    fila.push((start_state, []))
    while not fila.isEmpty():
        state, actions = fila.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                new_actions = actions + [action]
                fila.push((successor, new_actions))

    return []


    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    #PROMPT: considerando el taller que te subi anteriormente, cree el siguiente codigo de uniformCostSearch. Ayudame a modificarlo para cumplir con el enunciado.
    """def uniformCostSearch(problem: SearchProblem):
    fila = utils.PriorityQueue()
    visited = set()
    start_state= problem.getStartState()
    fila.push((start_state, [], 0), 0)
    actions = []
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    
    while not fila.isEmpty():
        state, actions, costo = fila.pop()
        
        posibleObjetivo = problem.isGoalState(state)
        if posibleObjetivo == True:
            return actions
            print("llegué")
        
        else:
            if state not in visited:
                visited.add(state)
        
            sucesores = problem.getSuccessors(state)
            for successor, action, cost in sucesores:
                if successor not in visited:
                    visited.add(successor)
                    costs = costo + cost
                    actions = actions + action
                    fila.push((successor, actions, cost), costs)
                
    return []
    """
    # TODO: Add your code here
    fila = utils.PriorityQueue()
    visited = set()

    # Cada elemento del stack será: (estado, lista_de_acciones)
    start_state = problem.getStartState()
    fila.push((start_state, [], 0),0)

    while not fila.isEmpty():
        state, actions, costo = fila.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                nuevo_costo=costo+cost
                new_actions = actions + [action]
                fila.push((successor, new_actions, nuevo_costo),nuevo_costo)

    return []
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    #PROMPT: considerando el taller que te subi anteriormente, cree el siguiente codigo de aStarSearch. Ayudame a modificarlo para cumplir con el enunciado.
    """def aStarSearch(problem: SearchProblem):
    fila = utils.PriorityQueue()
    visited = set()
    start_state= problem.getStartState()
    fila.push((start_state, [], 0), 0)
    actions = []
    
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    
    while not fila.isEmpty():
        state, actions, costo = fila.pop()
        
        posibleObjetivo = problem.isGoalState(state)
        if posibleObjetivo == True:
            return actions
            print("llegué")
        
        else:
            if state not in visited:
                visited.add(state)
        
            sucesores = problem.getSuccessors(state)
            for successor, action, cost in sucesores:
                if successor not in visited:
                    visited.add(successor)
                    CostoHeuristica = costo + heuriscic(successor, problem)
                    costs = costo + cost
                    actions = actions + action
                    fila.push((successor, actions, costs), CostoHeuristica)
                    
    return []

    """
    # TODO: Add your code here
    fila = utils.PriorityQueue()
    visited = set()

    # Cada elemento del stack será: (estado, lista_de_acciones)
    start_state = problem.getStartState()
    fila.push((start_state, [], 0),0)

    while not fila.isEmpty():
        state, actions, costo = fila.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.getSuccessors(state):
                new_actions = actions + [action]
                CostoHeuristica=costo+heuristic(successor, problem)
                nuevo_costo=costo+cost
                fila.push((successor, new_actions, nuevo_costo),CostoHeuristica)

    return []
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
