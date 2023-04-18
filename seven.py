from queue import Queue

def jug_problem(start, goal):
    q = Queue()
    q.put(start)
    came_from = {}
    came_from[start] = None
    
    while q:
        current = q.get()

        if current == goal:
            break

        a, b = current
        next_states = [(4, b), (a, 3), (0, b), (a, 0), (min(a+b, 4), max(0, a+b-4)), (max(0, a+b-3), min(a+b, 3))]
        
        for next_state in next_states:
            if next_state not in came_from:
                q.put(next_state)
                came_from[next_state] = current
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

[print(i) for i in jug_problem((0,0), (2,0))]

