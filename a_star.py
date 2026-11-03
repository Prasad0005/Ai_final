def h(state):
    goal = [1,2,3,4,5,6,7,8,0]
    return sum(state[i] != goal[i] and state[i] != 0
               for i in range(9))

def astar(start):
    goal = [1,2,3,4,5,6,7,8,0]
    open_list = [(h(start), start)]

    while open_list:
        open_list.sort()
        cost, state = open_list.pop(0)

        if state == goal:
            print("Goal Reached:", state)
            return

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if 0 <= new < 9 and not (move == -1 and zero % 3 == 0) and not (move == 1 and zero % 3 == 2):
                s = state.copy()
                s[zero], s[new] = s[new], s[zero]

                if s not in [x[1] for x in open_list]:
                    open_list.append((h(s), s))
                    
start = [1,2,3,4,0,6,5,8,7]
astar(start)