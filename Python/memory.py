"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""
# Import necessary libraries
from random import *
from turtle import *
from freegames import path

# Game elements
grid_dim = 4 # grid dimension
sqr_len = 400 / grid_dim # tile length

car = path('car.gif')
tiles = list(range(int(grid_dim**2 / 2))) * 2
state = {'mark': None}
hide = [True] * grid_dim**2

# Function that draws one tile
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()

    # Draw each side of the square
    for count in range(4):
        forward(sqr_len)
        left(90)
    end_fill()

# Function that converts tile coordinates to an index
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // sqr_len + ((y + 200) // sqr_len) * grid_dim)

# Function that converts tile count to coordinates
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % grid_dim) * sqr_len - 200, (count // grid_dim) * sqr_len - 200

# Function that executes the necessary actions for a tile click or tap
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark'] 

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot # change state of 'mark' to the tile's index
    else:
        hide[spot] = False # the index changes to a not hidden state
        hide[mark] = False
        state['mark'] = None # reset the state of 'mark'

# Function that draws the background image and tiles 
def draw():
    "Draw image and tiles."
    # Draw background image
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Draw a white tile for each index that is hidden 
    for count in range(grid_dim**2):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # If mark has an index and the tile is hidden, draw the corresponding number 
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
