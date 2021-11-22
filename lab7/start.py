def add_edge(graph, edge):
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    dictinary = []
    if edge[0] not in graph:
        graph_update = {edge[0]: []}
        graph.update(graph_update)
    if edge[1] not in graph:
        graph_update = {edge[1]: []}
        graph.update(graph_update)
    graph_keys = list(graph.keys())
    graph_val = list(graph.values())

    if edge[0] not in graph_val[edge[1] - 1]:
        graph_val[edge[1] - 1].append(edge[0])
    if edge[1] not in graph_val[edge[0] - 1]:
        graph_val[edge[0] - 1].append(edge[1])

    graph_keys.append(edge[1])
    for i in range(len(graph)):
        dictinary.append([graph_keys[i], graph_val[i]])
    return dict(dictinary)
print(add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7)))