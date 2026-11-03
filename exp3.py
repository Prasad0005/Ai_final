
from heapq import heappush, heappop

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(abs(i//3 - (v-1)//3) +
            abs(i%3 - (v-1)%3)
            for i, v in enumerate(s) if v)

pq = [(h(start), 0, start, [])]
seen = set()

while pq:
    f, g, s, path = heappop(pq)

    if s == goal:
        for state in path + [s]:
            print(state[0:3], state[3:6], state[6:9])
            print()
        break

    if s in seen:
        continue
    seen.add(s)

    z = s.index(0)

    for d in [-3, 3, -1, 1]:
        n = z + d

        if 0 <= n < 9 and not (
            (d == -1 and z % 3 == 0) or
            (d == 1 and z % 3 == 2)
        ):
            t = list(s)
            t[z], t[n] = t[n], t[z]
            t = tuple(t)

            if t not in seen:
                heappush(pq, (g + 1 + h(t), g + 1,
                        t, path + [s]))
