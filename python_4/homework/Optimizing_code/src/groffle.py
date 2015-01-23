""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_fast(mass, density):
    return sum(map((log(mass * density)).__truediv__, range(1,10001)))

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

mass = 2.5 
density = 12.0 

if __name__ == "__main__":

    timer_fast = Timer("total = groffle_fast(mass, density)", 
     "from __main__ import groffle_fast, mass, density") 
    print("time (fast):", timer_fast.timeit(number=1000))
    print(groffle_fast(mass, density))

    timer_slow = Timer("total = groffle_slow(mass, density)", 
     "from __main__ import groffle_slow, mass, density") 
    print("time (slow):", timer_slow.timeit(number=1000))
    print(groffle_slow(mass, density))

    import cProfile as profile
    profile.run('groffle_slow(mass, density)', 'profiledata_slow')
    profile.run('groffle_fast(mass, density)', 'profiledata_fast')
