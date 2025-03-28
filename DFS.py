# Simple example of DFS with an irregular tree
g = [[1, 2, 3], [4], [5, 6, 7], [8], [9, 10], [], [11, 12], [13], [14], [], [15, 16], [], [17], [], [18], [], [], [], []]


def DFS(graph, visited=[], stack=[0]):
    if stack == []:
        print(visited)
    else:
        top = stack[-1]
        stack.pop(-1)
        visited.append(top)
        turn = reversed(graph[top])
        for i in turn:
            stack.append(i) 
        return DFS(graph, visited, stack)

DFS(g, [], [0])
