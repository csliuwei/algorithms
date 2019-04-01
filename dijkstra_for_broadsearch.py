
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
    graph['cab'] = {}
    graph['cat'] = {}
    graph['car'] = {}
    graph['mat'] = {}
    graph['bat'] = {}
    graph['bar'] = {}

    graph['cab']['cat'] = 1
    graph['cab']['car'] = 1
    graph['cat']['mat'] = 1
    graph['cat']['bat'] = 1
    graph['car']['cat'] = 1
    graph['car']['bar'] = 1
    graph['mat']['bat'] = 1
    graph['bar']['bat'] = 1

    parents['cat'] = 'cab'
    parents['car'] = 'cab'

    costs = {}
    costs['cat'] = 1
    costs['car'] = 1
    costs['mat'] = float('inf')
    costs['bar'] = float('inf')
    costs['bat'] = float('inf')

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

    print('The lowest cost to end is {}'.format(costs['bat']))

    path_list = []
    item = 'bat'
    path_list.append(item)
    while item != 'cab':
        item = parents[item]
        path_list.append(item)

    path_list.reverse()

    print('The shortest path is: ')
    path_string = ''
    for item in path_list:
        if item != 'bat':
            path_string = path_string + item + ' --> '
        else:
            path_string = path_string + item 
    print(path_string)



