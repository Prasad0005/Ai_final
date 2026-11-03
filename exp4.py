
def hanoi(n, source, helper, dest):
    if n == 1:
        print(source, "->", dest)
        return

    hanoi(n-1, source, dest, helper)
    print(source, "->", dest)
    hanoi(n-1, helper, source, dest)

hanoi(3, 'A', 'B', 'C')
