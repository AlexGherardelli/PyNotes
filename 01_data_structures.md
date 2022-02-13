 # Data structures and methods

# TODO
**Lists**
- Adding Values to Lists with the append() and insert() Methods
- Sorting the Values in a List with the sort() Method

**Strings** 
- Something on strings

**Dictionaries**
- Sorting

**Tuples**
- zip method? 

**Sets**
- add
- intersection
- union
- from list to sets and viceversa



## Lists
Lists are mutable collections of items. 


### List manipulation
**Can be accessed through index**
```python
lst = ["apple", "banana", "tomato"]
lst[0] # get first item: apple
lst[-1] #get last item: tomato
 
```
**Can be sliced with ```[:]``` operator**
```python
lst = ["apple", "banana", "tomato"]
lst[1:] # get all list from second item "banana" onwards
lst[:1] # get only first time (from 0 to 1 index, not includding it)
```
**The ```[:]``` operator is very useful to reverse a list**
```python
lst = ["apple", "banana", "tomato"]
lst[::-1] # reverse list ["tomato", "banana", "apple]

lst1 = lst.reverse() # Method 2

```
**List concatenation**
Two lists can be concatenated using the ```+ operator``` or the ```extend method```
```python
fruits = ["apple", "banana", "peach"]
vegetables = ["salad", "zucchini", "cucumber"]

# Method 1: create new list with two list concatenated
fruits_and_vegetables = fruits + vegetables 

# Methods 2: adds second list to first
fruits.extend(vegetables)
```

**Copying a list (shallow copy)**
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original.

```python
lst = [1, 2, 3]
# Method 1: Using slicing operator
lst_copy = lst[::]
# Method 2: Using the copy method
lst_copy = lst.copy()

# Method 3: Create another list
lst_copy = list(lst)
```
NB: Shallow copies are just one level deep. They work fine with list of one levels, but since they contain pointers to the original objects, they will start behaving "weirdly" for nested lists
```python
lst = [[1, 2, 3], [4, 5, 6]]
lst2 = lst[::] # Shallow copy

# Modifies original list
lst[0][1] = ["a", "b"]

print(lst2) # return [[1, ['a', 'b'], 3], [4, 5, 6]] 

```

**Copying a list (Deep copy)**

The solution to the above problem is a deep copy. A deep copy makes the copying process recursive. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. Copying an object this way walks the whole object tree to create a fully independent clone of the original object and all of its children.

```python
# Method 1: Using deepcopy()

import copy

lst = [[1, 2, 3], [4, 5, 6]]
lst2 = copy.deepcopy(lst)

# Method 2: Using list comprehension
lst = [[1, 2, 3], [4, 5, 6]]
lst2 = []


```

**Remove items from lists**
Items from a list can be removed using ```del```, ```pop()```or ```remove()```. ```Del``` is a keyword, while ```pop``` and ```remove``` are built-in methods.

```python
# Method 1: Using del 
lst = ["apple", "banana", "orange"]

del lst[0] # removes item at n-th index (in this case, apple at index 0)
del lst # removes entire list

```

Both pop and remove can remove items in a list, but pop takes an *index* and remove takes a *value*.

```python
lst = ["apple", "banana", "orange"]

lst.pop(0) # removes item at n-th index (in this case, apple at index 0)
lst.remove("banana") # remove item called by its value
print(lst) # organge

```

### List comprehension
List comprehensions are a compact syntactic construct available in Python to create and manipulate lists. It is more time-efficient and space-efficient than using loops and requires less lines of code, making it ultimately more readable.

**Basic syntax** 
```
[expression for item in list]
```
 **Conditionals in list comprehension

 ```
 [expression for item in list if condition]
 ```

## Dictionaries

Dictionaries are  **mutable** data structures comprised of key-value pairs. They are good to quickly accessing data by its key. From Python 3.7 onward, the order of the dictionary is preserved.

### Creating dictionaries

```python

#  Method 1
d = dict(dog = 10, cat = 5, guinea_pig = 3) 

# Method 2
d = {"dog": 10, "cat": 5, "guinea_pig" : 3 }

# Method 3
d = {}
animals = ["dog", "cat", "guinea_pig"]
values = [10, 5, 3]
for k, v in zip(animals, values):
    d[k] = v

```

###  Dictionary shorthands

Similarly to list comprehensions, it is possible to create a new dictionary using dictionary comprehension, which is a shorthand for the methods illustrated above. 

Dictionary comprehension is a method for transforming one dictionary into another dictionary. During this transformation, items within the original dictionary can be conditionally included in the new dictionary and each item can be transformed as needed.

``` python
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Returns a new dictionary with all values from dict1 multiplied by 2
dict2 = {key: value * 2 for key, value in dict1.items()}

print(dict2) # {'a': 1, 'b': 4, 'c': 6, 'd': 8}

```
## Getting values from dictionaries

**Get keys: ```d.keys()```**
```python
d = {"dog": 10, "cat": 5, "guinea_pig" : 3 }

# get dictionary keys in dict_keys type
a = d.keys()
type(a) # dict_keys

# iterate through keys
for k in d.keys():
    print(k) # dog cat guinea_pig

# transform dict keys in list
b = list(d.keys()) # ['dog', 'cat', 'guinea_pig']

```
**Get values: ```d.values()```**
```python
d = {"dog": 10, "cat": 5, "guinea_pig" : 3 }

# get dictionary values in dict_value type
a = d.values()
type(a) # dict_values

# iterate through values
for v in d.values():
    print(v) # 10 5 3 

# transform dict value in list
b = list(d.values()) # [10, 5, 3]

```
**Get item by its key**

```python
d.get('dog') # 10
```

**Get key:value pairs**
```python
c = d.items() # dict_items([('dog', 10), ('cat', 5), ('guinea_pig', 3)])
type(c) # dict_items

```
## Looping over a dictionary
```python

# Get the key:value pairs
for k, v in d.items():
    print(k, v) 
# dog 10
# cat 5
# guinea_pig 3

# Get the index of the item and its keys
for i, v in enumerate(d):
    print(i, v)
    # 0 dog
    # 1 cat
    # 2 guinea_pig

```



### Updating dictionaries
**Add item to dictionary**
```python

```
**Update dictionary**
```python

```

**Remove item from dictionary**
```python

```

## Search into a dictionary
**Search a value in dictionary**

```python
db = [
    {'name': 'Paperino','surname':'Paolino',      'tel':'555-1313',  'address': 'via dei Peri 113',          'city ': 'Paperopoli'},
    {'name': 'Gastone', 'surname':'Paperone',     'tel':'555-1717',  'address': 'via dei Baobab 42',         'city ': 'Paperopoli'},
    {'name': 'Paperon', 'surname':"de' Paperoni", 'tel':'555-99999', 'address': 'colle Papero 1',            'city ': 'Paperopoli'},
    {'name': 'Archimede','surname':'Pitagorico',  'tel':'555-11235', 'address': 'colle degli Inventori 1',   'city ': 'Paperopoli'},
    {'name': 'Pietro',  'surname':'Gambadilegno', 'tel':'555-66666', 'address': 'via dei Ladri 13',          'city ': 'Topolinia'},
    {'name': 'Trudy',   'surname':'Gambadilegno', 'tel':'555-66666', 'address': 'via dei Ladri 13',          'city ': 'Topolinia'},
    {'name': 'Topolino','surname':'Mouse',        'tel':'555-12345', 'address': 'via degli Investigatori 1', 'city ': 'Topolinia'},
    {'name': 'Minnie',  'surname':'Mouse',        'tel':'555-54321', 'address': 'via di M.me Curie 1',       'city ': 'Topolinia'},
    {'name': 'Pippo',   'surname':"de' Pippis",   'tel':'555-33333', 'address': 'via dei Pioppi 1',          'city ': 'Topolinia'},
    ]

def search_columns(dictionary, query):
    result = []
    for record in dictionary:
        if 

# per cercare su piÃ¹ colonne
def cerca_multicolonna_lineare(ag, query):
    # IN : agenda, query: coppie colonna/valore (con un dizionario)
    # OUT: lista dei record che soddisfano tutte le condizioni
    # all'inizio l'elenco di record risultante Ã¨ []
    risultato = []
    # scandiamo l'agenda e per tutti i record
    for record in ag:
        # se corrispondono alla query
        if corrisponde_alla_query(record, query):
            # aggiungo il record all'output
            risultato.append(record)
    # torno l'elenco di record
    return risultato



```
## Tuples
Tuples are like lists and they can store all sorts of objects (e.g. strings, integers, dictionaries, other tuples), but they are **immutable**. 

They are useful when you want to group a bunch of values together (e.g. x y coordinates) and never change them.

## Strings
Strings are **immutable**, but there are a lot of useful methods for string manipulation. 

**Convert cases***
- str.lower()
- str.upper() 
- str.swapcases()
- str.capitalize()

**Check if string has a certain type**
- str.isspace(): checks if the caracters 
- str.isalpha(): checks if string is alphabetic
- str.isalfanum(): check if strings is alphanumeric
- str.isdigit(): check if string is number only

**Replace characters**
- str.replace("a", "b"): replace character "a", with character "b"
- str.translate() & str.maketrans()

**Remove spaces**
- str.strip(): remove leading and trailing whitespace
- str.rstrip():
- str.lstrip(): remove leading whitespace

**Split and join strings**
- str.split(self, /, sep=None, maxsplit=-1):  Return a list of the words in the string, using sep as the delimiter string
- str.splitlines(): split lines at new line
- str.join(self, iterable, /): Concatenate any number of strings. '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
- str.partition(self, sep, /): Partition the string into three parts using the given separator.



## Sets
Sets are a **mutable** type and they are very useful to remove duplicates in Python and to perform set operations like intersection and union 

```python
a = {1, 2, 3}
b = {(1, 2), 2, 3, 6, 'A'}

a.intersection(b) #  {2, 3}
a.union(b) # {(1, 2), 1, 2, 3, 6, 'A'}

```
**Convert nested lists into lists of sets**
It could be useful sometimes to convert list into sets. However, set require their items to be hashable. Out of types predefined by Python only the immutable ones, such as strings, numbers, and tuples, are hashable. 

Mutable types, such as lists and dicts, are not hashable because a change of their contents would change the hash and break the lookup code.

As a solution we can either:
- convert the inner lists in tuples
```python
lst = [[1, 2, 3], [3, 4, 5]]
lst = [tuple(el) for el in lst] # [(1, 2, 3), (3, 4, 5)]

new_set = set(lst)  # {(1, 2, 3), (3, 4, 5)}
```
- convert the inner lists to sets using list comprehensions
```python
lst = [[1, 2, 3], [4, 5, 6], [5, 1, 2]]
list_of_sets = [set(el) for el in lst] # [{1, 2, 3}, {4, 5, 6}, {1, 2, 5}]

```

- flatten the matrix, then convert it
```python
lst = [[1, 2, 3], [4, 5, 6], [5, 1, 2]]

flatten = [item for l in lst for item in l] # [1, 2, 3, 4, 5, 6, 5, 1, 2]

```

### Create set of sets
Similarly, sets are **mutable** data types: directly trying to create a set of set will result into an ```unhashable type``` error.

Solutions are:

**Using ```frozensets```**
- using ```frozensets```, which are a set built-in in Python. Does everything that the "regular" set does, but it's immutable and hashable
```python
lst = [[1, 2, 3], [4, 5, 6], [5, 1, 2]]
list_of_frozensets = [frozenset(item) for item in lst] #  [frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({1, 2, 5})]
set_of_sets = set(list_of_frozensets) #  {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({1, 2, 5})}
