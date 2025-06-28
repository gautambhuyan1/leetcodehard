
def createGraph(dictionary: [str]) :

    for i in range(len(dictionary)):
        for j in range(len(dictionary)):
            if i == j:
                continue
            w1 = dictionary[i]
            w2 = dictionary[j]

            diff = 0

            #print("Comparing:", i, j, w1, w2, graph[i][j])

            for k in range(len(w1)):
                if w1[k] != w2[k]:
                    diff += 1
            if diff <= 1:
                graph[i][j] = 1
                graph[j][i] = 1

    return 

def qualify(a: str, b: str) -> bool:

    diffCount = 0 

    for i in range(len(a)):
        if a[i] != b[i]:
            diffCount += 1
    if diffCount <= 1:
        return True
    return False

def shortestPath(p1: str, p2: str, dict: [str], graph: [[int]]) -> [int]:

    start = dict.index(p2)
    stack = []
    stkPtr = -1
    dictLen = len(dict)
    parent = [0 for _ in range(dictLen)]

    visited = [0 for _ in range(dictLen)]

    j = start
    done = False
    depth = 0

    visited[start] = 1

    while done == False:
        for i in range(dictLen):
            if i == j:
                continue
            #print("Current node:", dict[j], "Target node", dict[i], "Connected:", graph[j][i], "Stack :", stack, "Visited: ", visited)
            if graph[j][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(i)
                stkPtr += 1
                parent[i] = j
                #print("### Parent of", dict[i], "is", dict[j])
                
                if qualify(dict[i], p1):
                    #print("Found a match:", dict[i], "Parent:", p1)
                    k = i
                    print(p1)
                    
                    while parent[k] != 0:
                        print(dict[k])
                        k = parent[k]
                    print(p2)
                    done = True
                    return parent        
        depth += 1
        if depth > dictLen:
            return []
        if stkPtr > -1:
            j = stack[stkPtr]
            stkPtr -= 1
        else:
            done = True
    return []


dict = ["pot", "hot", "cot", "got", "pit", "lop", "sop", "log", "cog", "dog", "dot", "lot"]

graph = [[0 for _ in range(len(dict))] for _ in range(len(dict))]

createGraph(dict)

P1 = "pot"
P2 = "sop"

print(P1, " to ", P2, " in dictionary: ", dict)

path = shortestPath(P1, P2, dict, graph)
#print("Shortest path from", P1, "to", P2, ":", path)
