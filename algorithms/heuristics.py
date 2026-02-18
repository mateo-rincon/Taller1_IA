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
    # TODO: Add your code here
    utils.raiseNotDefined()
