
'''
Useful code from Lecture 14 - Masi
'''
import image


# %% BUILD MATRIX
def create_matrix_short(rows, cols, value = 0):
    '''
    Create matrix with for loops and 
    '''
    matrix = []
    for row in range(rows):
        matrix.append([value] * cols)
    return matrix

def create_matrix_short(rows, cols, value = 0):
    '''
    Create matrix with list comprehension
    '''
    matrix = [ [value] * cols for row in range(rows) ]
    return matrix

def create_matrix_short(rows, cols, value = 0):
    '''
    Create matrix with map and lambda fuction
    '''
    return list(map(lambda row: [value] * cols, range(rows)))


# %% USING MATRICES TO CREATE IMAGES
colormap = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (0, 0, 0),
    "black": (255, 255, 255),
    "cyan" : (  0, 255, 255),
"magenta" : (255,   0, 255),
"yellow" : (255, 255,   0)
}

color_mat = create_matrix_short(256, 256, colormap['black'])

# %% LINEE SU ASSI

def plot_line_h(matrix, x, y, length, value):
    matrix[y][x: x + length] = [value] * length

def plot_line_v(matrix, x, y, length, value):
    for each_y in range(y, y+length):
        matrix[each_y][x] = value

# CREATES A RED CROSS IN 
plot_line_v(color_mat, 128, 64, 129, colormap["red"])
Image(color_mat)

# %% DRAW RECTANGLE


def draw_rect(x, y, width, length):
    '''
    To draw a rectangle, I need to know the position of the top-left corner (y, x), its width and length
    '''
    def clip(v, min_v, max_v):
        return  min(max(min_v, v ), max_v)