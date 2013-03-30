import itertools


def triangle_sum(length_of_tri,triangle):
    routes = itertools.combinations_with_replacement((0,1)*6,length_of_tri)
    
    array = load_triangle(triangle)
    routes = set(routes)
    print len(routes)
    
    totalsum = 0
    for route in routes:
        index = 0
        arrindex = 0
        sum = 0
        for arr in array:
            step = route[index]
            arrer = arr[arrindex]
            sum+=arrer
            index +=1
            arrindex += step
        if sum > totalsum:
            totalsum = sum
            print totalsum
    print totalsum
            
        
    
def load_triangle(file):
    array = []
    with open(file) as file:
        for line in file.read().split('\n'):
            array.append(list(int(n) for n in line.split(" ")))
    return array

triangle_sum(15,"Euler18.txt")                

if __name__ == '__main__':
    pass