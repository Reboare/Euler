if __name__ == "__main__":
    var = range(1,101)
    print(sum(var)**2 - sum([i*i for i in var]))