# Snippets

## TODO
- Combinations and permutations
- Tournament 
- Non uscire dal bordo di una lista con modulo



## Flatten a list of lists (matrix)

**Iteratively**
```python

```

**Recursively**
```python
lst = [[1, 2, 3], [4, 5, 6], [5, 1, 2]]

def flatten(lst):
    if len(lst) == 0:
        return lst
    if type(lst[0]) == list:
        return flatten(lst[0] + flatten(lst[1:]))

    return  lst[:1] + flatten(lst[1:])
```