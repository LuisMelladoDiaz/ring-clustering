from asyncio.windows_events import NULL
from enum import Enum



def check_halting(iterations, convergence, max_iterations, min_convergence):
    halt = False
    if (iterations >= max_iterations):
        halt = True
    if(min_convergence != NULL and convergence <= min_convergence):
        halt = True
    return halt
