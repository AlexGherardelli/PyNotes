

#%% FIBONACCI AND RECURSION

# fib: 1, 1, 3, 5, 8, 13, ...


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return  1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# for n in range(1, 101):
#     print(n, ":", fibonacci(n))

#%% FIBONACCI WITH MEMOIZATION
fib_cache = {}
def fib(n):

    if n in fib_cache:
        return fib_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else: 
        value = fib(n-1) + fib(n-2)
    
    fib_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fib(n))

#%% MEMOIZATION WITH FUNCTOOL

# %%
from functools import lru_cache

@lru_cache(maxsize= 100)
def fibonacci(n: int):
    if n < 1:
        raise ValueError('n must be positive int')
    if type(n) != int:
        raise TypeError("n must be positive int")
    if n == 1:
        return 1
    elif n == 2:
        return  1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 101):
    print(n, ":", fib(n))
# %% SANTA CLAUS DELIVERY RECURSIVELY

houses =  ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_gifs(houses):
    if len(houses) == 1:
        house = houses[0]
        print(f"Delivering gift to {house}")
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        
        deliver_gifs(first_half)
        deliver_gifs(second_half)

deliver_gifs(houses)

#%% 
colors = [0, 255]

moves = []
for color in colors:
    for i, j in enumerate(colors):
        moves.append((color, j))

print(moves)

from itertools import permutations




#%% 

# Write a function that takes an input n and sums all non-negative integers up to n
from functools import lru_cache

@lru_cache
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

@lru_cache(maxsize=1000)
def factorial(n):
    assert type(n) == int
    assert n > 0
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)