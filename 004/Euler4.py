def palindrome(xs):
    j = str(xs)
    return (j == j[::-1])

def main():
    maximum = 0
    for h in xrange(100,1000):
        for i in xrange(100, 1000):
            j = h*i 
            if palindrome(j) and j > maximum:
                maximum = j
    return maximum

if __name__ == '__main__':
    print main()
