import time 

def get_node_at_pos(row, col): 
    if (row < 0) or (col < 0) or (row > 7) or (col > 7): 
        return -1  
    return (8 * row) + col 
 
childNodes = {}
 
def get_children(node):
    global childNodes
    if(childNodes.has_key(node)): 
        return childNodes[node]
    row = (node / 8)
    col = (node % 8)
    children = []
    children.append(get_node_at_pos(row-2,col - 1)) 
    children.append(get_node_at_pos(row-1,col - 2)) 
    children.append(get_node_at_pos(row-2,col + 1)) 
    children.append(get_node_at_pos(row-1,col + 2)) 
    children.append(get_node_at_pos(row+2,col + 1)) 
    children.append(get_node_at_pos(row+1,col + 2)) 
    children.append(get_node_at_pos(row+2,col - 1)) 
    children.append(get_node_at_pos(row+1,col - 2)) 
        
    children = [x for x in children if x != -1] 
    childNodes[node] = children
    return children 

sp = {}
visited = []  
wq = []

def bfs_sp(start_node, end_node): 
    global sp
    global visited
    global wq
    while len(wq) > 0:
        curr_node = wq[0] 
        visited.append(curr_node) 
        if(curr_node == end_node): 
            return 
        children = get_children(curr_node)
        for child in children:
            if(curr_node == start_node): 
                curr_sp = 1 
            else:
                curr_sp = sp[curr_node] + 1 
            if(sp.has_key(child)): 
                if(sp[child] > curr_sp):
                    sp[child] = curr_sp
                    wq.append(child)
                else: 
                    if child not in visited: 
                        wq.append(child)
            else: 
                sp[child] = curr_sp 
                wq.append(child)
        wq.pop(0) 
    return          

def bfs(start_node, end_node):
    sp.clear() 
    del visited[:]
    del wq[:]
    
    if(start_node == end_node):
        return 0
    wq.append(start_node)
    bfs_sp(start_node, end_node)
    print sp[end_node]

def answer(src, dest): 
    return bfs(src,dest) 

answer(0,1) 
answer(19,36)