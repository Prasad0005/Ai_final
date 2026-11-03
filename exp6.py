
def dfs(a, b, path, seen):
    if (a, b) in seen:
        return False

    seen.add((a, b))
    path.append((a, b))

    if a == 2 or b == 2:
        print("Solution:", path)
        return True

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - min(a, 3 - b), b + min(a, 3 - b)),
        (a + min(b, 4 - a), b - min(b, 4 - a))
    ]

    for x, y in states:
        if dfs(x, y, path.copy(), seen):
            return True

    return False

dfs(0, 0, [], set())
