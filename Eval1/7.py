def UCS(graph, goal, start, weight):
    Path = []
    Queue = []

    for i in range(len(goal)):
        Path.append(10 ** 8)

    Queue.append([0, start])

    isVisited = {}
    count = 0

    while len(Queue) > 0:
        Queue.sort()
        p = Queue[-1]

        del Queue[-1]

        p[0] *= -1

        if p[1] in goal:

            index = goal.index(p[1])

            if Path[index] == 10 ** 8:
                count += 1

            if Path[index] > p[0]:
                Path[index] = p[0]

            del Queue[-1]

            Queue.sort()
            if count == len(goal):
                return Path

        if p[1] not in isVisited:
            for i in range(len(graph[p[1]])):
                Queue.append([(p[0] + weight[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        isVisited[p[1]] = 1
    return Path
