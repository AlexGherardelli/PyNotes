# Matrix manipulation

## TODO
- Breath-Search First: BSF is an algorithm used to answer the question "What are the minimum number of moves to solve a puzzle? 
- Depth-Search First: DSF is an algorithm used to answer the question "What is the shortest path to solve a puzzle?

```python

```
## Matrices as two-dimensional arrays
 
### Create an empty matrix
```python
def create_matrix(n):
    return [[] for j in range(n)]
```

### Create matrix filled with 0s

```python
# n x m matrix
def create_matrix(n, m):
    return [[0 for i in range(n)] for j in range(m)]
```

### Order Matrices

This snippet illustrate how to order a matrix by its rows
```python
def order_matrix_by_row(matrix)
    # get width of matrix (size of its rows)
    width = len(matrix[0])
    # flatten a matrix, using a temporary matrix
    m = []
    for i, row in enumerate(matrix):
        m.extend(row)
    # and sort it 
    m.sort()

    # recreate the matrix by looping into the flattened list
    # n elements at a time
    result = []
    for i in range(0, len(m), width):
        result.append(m[i:i+width])

    return result
```

This snippet illustrate how to order a matrix by its columns

```python
    # create an empty matrix the same size as the input
    result = [[] for _ in range(len(matrice))]

    # going through the rows
    for r in range(len(matrice[0])):
        # create a temporary storage per column 
        column = []
        # going through the columns
        for c, col in enumerate(matrix):
            # add to the column list a list with columns and rows inverted
            column.extend(matrix[c][r])
        # and sort it in-place
        column.sort()
        # recreate the matrix by adding the sorted matrix
        for i, _ in enumerate(result):
            result[i].extend(column[i])
    # and return the result
    return result

```



## TODO: Image manipulation

- Creating an empty picture
- Drawing a line
- Drawing a rectangle on a picture
- Cropping an image
- Rotating, flipping and mirroring an image
- Applying filters
- Finding an image within an image

