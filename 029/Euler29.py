cache = []
for a in range(2,101):
    for x in range(2,101):
        if cache.count(a**x) == 0:
            cache.append(a**x)

print len(cache)