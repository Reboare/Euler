def file_conversion(file):
    with open(file) as tri:
        triangle_array = tri.read().splitlines() #This takes the file specified and splits it based on where it's line ends
    for x in range(0,len(triangle_array)): #iterates over each part of the array splitting the values
        triangle_array[x] = str(triangle_array[x]).split(" ")
    for x in range(0,20):
        for y in range(0,20):
            triangle_array[x][y] = int(triangle_array[x][y])
    print(triangle_array)
        
    return triangle_array#sets the list as the the value to return by the function



def verticalmultiply(grid,xval):
    n = 0
    greatest = 0
    for multiply in range(0,17):
        product = grid[multiply][xval]*grid[multiply+1][xval]*grid[multiply+2][xval]*grid[multiply+3][xval] #multiple 4 vals in column against
        if product > greatest:
            greatest = product
    return greatest

def horizontalmultiply(grid,yval):
    n = 0
    greatest = 0
    for multiply in range(0,17):
        product = grid[yval][multiply]*grid[yval][multiply+1]*grid[yval][multiply+2]*grid[yval][multiply+3] #multiple 4 vals in column against
        if product > greatest:
            greatest = product
    return greatest

def crossmultiply(grid,yval):
    greatest = 0
    for multiply in range(0,17):
        product = grid[yval][multiply]*grid[yval-1][multiply+1]*grid[yval-2][multiply+2]*grid[yval-3][multiply+3] #multiple 4 vals in column against
        if product > greatest:
            greatest = product
    return greatest

data = file_conversion("grid.txt")
greatestval=0
for val in range(0,20):
    if verticalmultiply(data,val)> greatestval:
        greatestval = verticalmultiply(data,val)
    if  horizontalmultiply(data,val) > greatestval:
        greatestval = horizontalmultiply(data,val)
for val in range(0,17):
    if crossmultiply(data,val) > greatestval:
        greatestval = crossmultiply(data,val)

print(greatestval)
