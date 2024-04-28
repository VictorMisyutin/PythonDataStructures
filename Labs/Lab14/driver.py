# lab 14 program
def createGraph() :
    dict = {
    "A": {"B": 1, "C": 4, "D": 2},
    "B": {"A": 9, "E": 5},
    "C": {"A": 4, "F": 15},
    "D": {"A": 10, "F": 7},
    "E": {"B": 3, "J": 7},
    "F": {"C": 11, "D": 14, "K": 3, "G": 9},
    "G": {"F": 12, "I": 4},
    "H": {"J": 13},
    "I": {"G": 6, "J": 7},
    "J": {"H": 2, "I": 4},
    "K": {"F": 6}
    }
    return dict
print ()
print (createGraph())
print ()

# label the home vertex
home = "A"
# variable to find the shortest distance between vertices
path = {}
# variable to explore the neighboring vertices
adj_vertex = {}
# list to append unvisited vertices and remove visited vertices
queue = []
# variable to implement the created graph
graph = createGraph()

for node in graph :
    path[node] = float("inf")
    adj_vertex[node] = None
    queue.append(node)
path[home] = 0

while queue :
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)) :
        if path[queue[n]] < min_val :
            key_min = queue[n]
    min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    for i in graph[cur] :
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate :
            path[i] = alternate
            adj_vertex[i] = cur


# the destination vertex
print("Please select a key from the following values:")
print (createGraph().keys())
x = input()
print()
print (f"The path between A to {x}:")
print (x, end = " <-- ")
while True :
    x = adj_vertex[x]
    if (x is None) :
        print("")
        break
    print (x, end = " <-- ")
print ()