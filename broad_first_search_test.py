from collections import deque 

graph = {}
graph['cab'] = ['cat','car']
graph['cat'] = ['mat','bat']
graph['car'] = ['cat','bar']
graph['mat'] = ['bat']
graph['bar'] = ['bat']
graph['bat'] = {}

processed_nodes = []

node_list = deque()
node_list += graph['cab']

# from 'cab' to 'bat'
steps = 0

while len(node_list)!= 0:
    node_for_check = node_list.popleft()
    if node_for_check in processed_nodes:
        continue 
    processed_nodes.append(node_for_check)
    steps += 1
    if node_for_check == 'bat':
        print(steps)
        break
    else:
        node_list += graph[node_for_check]


