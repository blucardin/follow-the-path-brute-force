
def sequencefind():
    sequence = input("sequence:")

    n = 0

    for s in range(0, len(sequence)):

        if sequence[s] == "R":
            n = (2 * n) + 2    

        elif sequence[s] == "L":
            n = (2 * n) + 1
        
    print(n)

    global keepplaying
    keepplaying = input("keep playing? (y/n)")

sequencefind()
while keepplaying == "y":
    sequencefind()




