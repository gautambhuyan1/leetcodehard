
# Find the path from one to another in a dictionary, such that each adjascent word differs from the next by one character
# The Code first creates a graph of the dictionary where the nearest neighbors differ by maximum one character. Then if employs depth first search to find the laddar or words.


def qualify(a: str, b: str) -> int:

    diffCount = 0 

    for i in range(len(a)):
        if a[i] != b[i]:
            diffCount += 1
    
    return diffCount
    
def createGraph(dictionary: [str]) :

    for i in range(len(dictionary)):
        for j in range(i + 1, len(dictionary)):
            if i == j:
                continue
            w1 = dictionary[i]
            w2 = dictionary[j]

            if qualify(w1, w2) <= 1:
                graph[i][j] = 1
                graph[j][i] = 1

    return 


def shortestPath(p1: str, p2: str, dict: [str], graph: [[int]]) -> [int]:

    try :
        start = dict.index(p2)
    except ValueError:
        print("Error:", p2, "not in dictionary")
        return []

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
                
                q = qualify(dict[i], p1)
                if q <= 1:
                    print("The word laddar is as follows:")
                    k = i
                    if q == 1:
                        print(p1)
                    
                    while parent[k] != 0:
                        print(dict[k])
                        k = parent[k]
                    print(p2)
                    done = True
                    return parent   # if the printing business needs to happen in the caller function     
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

P1 = "lop"
P2 = "cog"

print(P1, " to ", P2, " in dictionary: ", dict)

path = shortestPath(P1, P2, dict, graph)
if not path:
    print("No path found from", P1, "to", P2)
#print("Shortest path from", P1, "to", P2, ":", path)
