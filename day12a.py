with open("day12.txt") as f:
    lines = f.readlines()

def multi_visit(node):
    return node == node.upper()

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

def trace(graph, track):
    if track[-1] == 'end':
        return 1
    if not track[-1] in graph:
        return 0
    number = 0
    for option in graph[track[-1]]:
        if not multi_visit(option) and option in track:
            continue
        else:
            number += trace(graph, track + [option])
    return number

def process(lines):
    graph = read_graph(lines)
    number = trace(graph, ["start"])
    return number

assert process("""start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".splitlines()) == 10

assert process("""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".splitlines()) == 19

assert process(lines) == 3887

print(process(lines))
