"""
Program that uses timeit module to show the difference between a list comprehension
and the list() function as applied to large sequences of random numbers.
"""
from random import sample
from timeit import Timer

def rand_gen():
    "Generates a random number from a list of one million random numbers"
    rand_lst = sample(range(1, 1000001), 1000000)
    for i in rand_lst:
        yield i

if __name__ == "__main__":
    
    rand_lst_timer_comprehension = Timer("[x for x in sample(range(1, 1000001), 1000000)]", "from __main__ import sample") 
    print("random list time (list comprehension):", rand_lst_timer_comprehension.timeit(number=1))
    
    rand_lst_timer_function = Timer("list(x for x in sample(range(1, 1000001), 1000000))", "from __main__ import sample") 
    print("random list time (list function):", rand_lst_timer_function.timeit(number=1))
    
    rand_gen_timer_comprehension = Timer("[x for x in rand_gen()]", "from __main__ import rand_gen") 
    print("random gen time (list comprehension):", rand_gen_timer_comprehension.timeit(number=1))
    
    rand_gen_timer_function = Timer("list(x for x in rand_gen())", "from __main__ import rand_gen") 
    print("random gen time (list function):", rand_gen_timer_function.timeit(number=1))
