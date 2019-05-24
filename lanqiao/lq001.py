l = [1, 3, 5, 8]
count = 0
for x in l:
    for y in l:
        for z in l:
            if x != y and x != z and y != z:
                count += 1
                print (x, y, z)
print count
