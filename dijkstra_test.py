
def find_lowest_cost(costs):
    cost = float('inf')
    node_name = None
    for key, val in costs.items():
        if key in processed_nodes:
            continue 
        elif val < cost:
            cost = val
            node_name = key 
    return node_name 

if __name__=='__main__':
    processed_nodes = []
    parents = {}

    graph = {}
    graph['start'] = {}
    graph['a'] = {}
    graph['b'] = {}
    graph['c'] = {}
    graph['d'] = {}
    graph['end'] = {}

    graph['start']['a'] = 5
    graph['start']['b'] = 2
    graph['a']['c'] = 4
    graph['a']['d'] = 2
    graph['b']['a'] = 8
    graph['b']['d'] = 7
    graph['c']['d'] = 6
    graph['c']['end'] = 3
    graph['d']['end'] = 1

    parents['a'] = 'start'
    parents['b'] = 'start'

    costs = {}
    costs['a'] = 5
    costs['b'] = 2
    costs['c'] = float('inf')
    costs['d'] = float('inf')
    costs['end'] = float('inf')

    node_name = find_lowest_cost(costs)
    while node_name is not None:
        print(node_name)
        cost = costs[node_name]
        neighbors = graph[node_name]
        for item in neighbors.keys():
            new_cost = cost + neighbors[item]
            if new_cost < costs[item]:
                costs[item] = new_cost 
                parents[item] = node_name 
        processed_nodes.append(node_name)
        node_name = find_lowest_cost(costs)

    print(graph)
    print(parents)
    print(costs)

    print('The lowest cost to end is {}'.format(costs['end']))

    path_list = []
    item = 'end'
    path_list.append(item)
    while item != 'start':
        item = parents[item]
        path_list.append(item)

    path_list.reverse()

    print('The shortest path is: ')
    path_string = ''
    for item in path_list:
        if item != 'end':
            path_string = path_string + item + ' --> '
        else:
            path_string = path_string + item 
    print(path_string)



