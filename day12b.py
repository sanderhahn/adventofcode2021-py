with open("day12.txt") as f:
    lines = f.readlines()

def multi_visit(node, twice = None):
    return node == node.upper() or node == twice

def read_graph(lines):
    graph = {}
    for line in lines:
        [start, end] = line.strip().split("-")
        if not start in graph:
            graph[start] = []
        graph[start].append(end)
        if not end in graph:
            graph[end] = []
        graph[end].append(start)
    return graph

def trace(graph, track, twice):
    if track[-1] == 'end':
        if twice == None or track.count(twice) == 2:
            return 1
        return 0
    if not track[-1] in graph:
        return 0
    number = 0
    for option in graph[track[-1]]:
        if option == twice and track.count(twice) == 2:
            continue
        if not multi_visit(option, twice) and option in track:
            continue
        else:
            number += trace(graph, track + [option], twice)
    return number

def process(lines):
    graph = read_graph(lines)
    twices = set(filter(lambda node: not multi_visit(node), graph.keys()))
    twices -= set(["start", "end"])
    number = 0
    number += trace(graph, ["start"], None)
    for twice in twices:
        number += trace(graph, ["start"], twice)
    return number

assert process("""start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".splitlines()) == 36

assert process(lines) == 104834

print(process(lines))
