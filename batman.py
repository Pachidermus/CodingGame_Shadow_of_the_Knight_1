import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

def get_half_jump(limit, position):
    """Return the size of the optimal jump on one axis given
    the position of the furthest away window in the research area
    and batman's location. 

    Args:
        limit::int
            position of the furthest away window in the research area.
        position::int
            position of batman.

    Returns:
        result::int
            size of the optimal jump on one axis.
    """
    return math.ceil(abs(limit-position) / 2)

# Set up initial area of research
min_x, max_x = 0, w
min_y, max_y = 0, h

x = x0
y = y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from Batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Reset jumps
    jump_x = 0
    jump_y = 0

    # Handle vertical jump
    if "U" in bomb_dir:
        max_y = y
        jump_y = -get_half_jump(min_y, y)

    if "D" in bomb_dir:
        min_y = y
        jump_y = get_half_jump(max_y, y)

    # Handle horizontal jump 
    if "L" in bomb_dir:
        max_x = x
        jump_x = -get_half_jump(min_x, x)

    if "R" in bomb_dir:
        min_x = x
        jump_x = get_half_jump(max_x, x)

    # Update batman's position
    x = x + jump_x
    y = y + jump_y

    # the location of the next window Batman should jump to.
    print(f"{x} {y}")