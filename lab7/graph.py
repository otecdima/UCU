"""Graph"""
def get_graph_from_file(file_name):
    """ 
    (str) -> (list)
    
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]

    """
    with open(file_name, 'r', encoding = 'utf-8') as new_file:
        final_list = []
        for str_ing in new_file:
            str_ing = str_ing.strip()
            str_ing = str_ing.replace(",", "")
            new_list = []
            for item in str_ing:
                new_list.append(int(item))
            final_list.append(new_list)
    return final_list

def to_edge_dict(edge_list):
    """ 
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    newset = {}
    for item in edge_list:
        len_of_element = len(item)
        for jtem in range (len_of_element):
            if item[jtem] in newset:
                if jtem == 1:
                    newset[item[jtem]].append(item[0])
                elif jtem == 0:
                    newset[item[jtem]].append(item[1])
            if item[jtem] not in newset:
                if jtem == 1:
                    newset.setdefault(item[jtem], [item[0]])
                if jtem == 0:
                    newset.setdefault(item[jtem], [item[1]])
    for item1 in newset:
        new_list = newset[item1]
        new_list = new_list.sort()
    return newset

def is_edge_in_graph(graph, edge):
    """ 
    (dict, tuple) -> bool
    
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    graph_value = graph.values()
    list_of_graphs = list(graph_value)
    element_of_edge = edge[0] - 1
    if edge[1] not in list_of_graphs[element_of_edge]:
        return False
    else:
        return True

def add_edge(graph, edge):
    """ 
    (dict, tuple) -> dict
    
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[1] not in graph:
        graph.update({edge[1]: []})
    if edge[0] not in graph:
        graph.update({edge[0]: []})
    graph_valuess = graph.values()
    new_graph_of_valuess = list(graph_valuess)
    graph_keyss = graph.keys()
    new_graph_of_keyss = list(graph_keyss)
    element_of_graph1 = edge[0] - 1
    element_of_graph2 = edge[1] - 1
    new_graph_of_valuess[element_of_graph1].append(edge[1])
    new_graph_of_valuess[element_of_graph2].append(edge[0])
    new_dict12 = dict(zip(sorted(new_graph_of_keyss), new_graph_of_valuess))
    return new_dict12
print(add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7)))

def del_edge(graph, edge):
    """ 
    (dict, tuple) -> (dict)
    
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    try:
        keys1 = list(graph.keys())
        values1 = list(graph.values())
        val1 = edge[1] - 1 
        val2 = edge[0] - 1 
        values1[val1].remove(edge[0])
        values1[val2].remove(edge[1])
        res = dict(zip(keys1, values1))
        return res
    except IndexError:
        return graph
    except ValueError:
        return graph

def add_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    of_value = graph.values()
    of_key = graph.keys()
    value_of_graph = list(of_value)
    key_of_graph = list(of_key)
    if node in key_of_graph:
        return graph
    else:
        key_of_graph.append(node)
        value_of_graph.append([])
        new_dict1 = dict(zip(key_of_graph, value_of_graph))
    return new_dict1
print(add_node({1: [2], 2: [1]}, 1))

def del_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    try:
        of_values = graph.values()
        values_of_graph = list(of_values)
        of_keys = graph.keys()
        values_of_graph.pop(node-1)
        keys_of_graph = list(of_keys)
        keys_of_graph.remove(node)
        for item in values_of_graph:
            for item1 in item:
                if item1 == node:
                    item.remove(node)
        new_dict = dict(zip(keys_of_graph, values_of_graph))
        return new_dict
    except IndexError:
        return graph

def convert_to_dot(graph):
    """ 
    (dict) -> (None)
    
    Save the graph to a file in a DOT format.
    """
    with open("lab_8.dot", "w", encoding='utf-8') as file:
        file.write("graph {\n")
        for i in graph.keys():
            for j in graph[i]:
                file.write("\t")
                file.write(j)
                file.write(" -- ")
                file.write(i)
                file.write("\n")


# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())