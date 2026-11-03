def hanoi(n):
    rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    moves = 2**n - 1

    if n % 2 == 0:
        dest = 'B'
    else:
        dest = 'C'

    for i in range(1, moves + 1):
        if i % 3 == 1:
            a, b = 'A', dest
        elif i % 3 == 2:
            a, b = 'A', 'C' if dest == 'B' else 'B'
        else:
            a, b = 'B', 'C' if dest == 'B' else 'B'

        if not rods[a] or (rods[b] and rods[a][-1] > rods[b][-1]):
            a, b = b, a

        rods[b].append(rods[a].pop())
        print("Move disk from", a, "to", b)
        
hanoi(3)