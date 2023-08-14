def print_grid(grid_size_x, grid_size_y):
    for _ in range(grid_size_y):
        print_horizontals(grid_size_x)
        print_verticals(grid_size_x)
    print_horizontals(grid_size_x)

def print_verticals(grid_size_x):
    vertical_string = "|"
    for _ in range(grid_size_x):
        vertical_string += "   |"
    print(vertical_string)

def print_horizontals(grid_size_x):
    horiz_string = ""
    for _ in range(grid_size_x):
        horiz_string += " ---"
    print(horiz_string)

grid_size_x = 3
grid_size_y = 5
print_grid(grid_size_x, grid_size_y)
