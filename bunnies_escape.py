ChildNodes = {}
Grid = []
ShortestPath = {}
Visited = []
WorkQueue = []
UnviableNodes = []

def get_node_at_pos(row, col, height, width):
    maxrow = height - 1
    maxcol = width - 1
    if (row < 0) or (col < 0) or (row > maxrow) or (col > maxcol):
        return ()
    return (row,col)

def get_children(node,height,width):
    global ChildNodes
    if(ChildNodes.has_key(node)):
        return ChildNodes[node]
    row = node[0]
    col = node[1]
    children = []
    children.append(get_node_at_pos(row,col - 1, height, width))
    children.append(get_node_at_pos(row,col + 1, height, width)) 
    children.append(get_node_at_pos(row + 1,col, height, width)) 
    children.append(get_node_at_pos(row - 1,col, height, width)) 
    children = [x for x in children if x != ()] 
    ChildNodes[node] = children
    return children 

def get_viable_children(node, height, width): 
    children = get_children(node, height, width) 
    children = [x for x in children if x not in UnviableNodes]
    return children 
    

def get_weight(node):
    return Grid[node[0]][node[1]]
    
def update_node(weight):
    if(weight == -1): 
        return -1 
    else:   
        return weight + 1
        
def better_path(a,b):
    if(a == -1): 
        return b
    if(b == -1): 
        return a
    if(a < b): 
        return a
    return b 
        
def viable(child): 
    if(child in WorkQueue): 
        return False
    if(child not in ShortestPath): 
        return True 
    if(ShortestPath[child][0] is not -1) or (ShortestPath[child][1] is not -1): 
        return True
    return False

def bfs_sp(start_node, end_node, height, width): 
    global ShortestPath
    global Visited
    global WorkQueue

    while len(WorkQueue) > 0:
        curr_node = WorkQueue[0]
        Visited.append(curr_node)
        """print("Visiting:" + str(curr_node)) """
        if(curr_node == end_node): 
            return 
        children = get_children(curr_node,height,width)
        if(curr_node == start_node): 
            ShortestPath[curr_node] = (0,0)
        for child in children:
            """ print("     Child: " + str(child)) """ 
            if(curr_node == start_node): 
                if get_weight(child) == 0: 
                    curr_sp = (1,-1)
                else:
                    curr_sp = (-1,1) 
            else:
                if get_weight(child) == 0: 
                    curr_sp = (update_node(ShortestPath[curr_node][0]), update_node(ShortestPath[curr_node][1]))
                else: 
                    curr_sp = (-1, update_node(ShortestPath[curr_node][0]))
            if(ShortestPath.has_key(child)): 
                zero_path = better_path(ShortestPath[child][0], curr_sp[0])
                one_path =  better_path(ShortestPath[child][1], curr_sp[1])
                new_sp = (zero_path, one_path)
                if (new_sp is not ShortestPath[child]): 
                    """ print("         Update SP: " + str(new_sp))  """  
                    ShortestPath[child] = new_sp
                    if viable(child): 
                        WorkQueue.append(child)
                else: 
                    if (child not in Visited) and viable(child): 
                        WorkQueue.append(child)
            else: 
                ShortestPath[child] = curr_sp 
                """ print("         New SP: " + str(curr_sp)) """  
                if(viable(child)): 
                    WorkQueue.append(child)
        WorkQueue.pop(0) 
    return  

def bfs(height,width):
    global ShortestPath
    global UnviableNodes
    ShortestPath.clear() 
    ChildNodes.clear()
    del Visited[:]
    del WorkQueue[:]

    start_node = (0,0)
    end_node = (height - 1, width - 1)
    if(start_node == end_node):
        return 1
    
    for i in range(0, height-1): 
        for j in range(0, width - 1): 
            is_viable = False
            node_weight = get_weight((i,j))
            if(node_weight == 1): 
                for child in get_children((i,j), height, width):
                    if get_weight(child) == 0: 
                        is_viable = True
                if(is_viable == False):  
                    UnviableNodes.append((i,j))
  
    WorkQueue.append(start_node)
    bfs_sp(start_node, end_node, height, width)
    if (end_node not in ShortestPath): 
        return 0

    fsp = ShortestPath[end_node]
    weight = better_path(fsp[0], fsp[1]) 
    return weight + 1
                        
def answer(maze):
    global Grid
    Grid = maze
    print bfs(len(Grid),len(Grid[0]))

maze1 = [ 
 [0, 0, 0, 0, 0, 0], 
 [1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1], 
 [1, 0, 0, 0, 0, 0]
]

maze2 = [
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

maze3 = [                                                                                                                                                                                                                                    
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

answer(maze2)
"""answer(maze2)"""

#include <iostream>
#include <vector>

using namespace std;

typedef struct _Meeting { 
  int startTime; 
  int endTime; 
} Meeting;  

int HasOverLap(Meeting a, Meeting b) { 
    if((a.startTime == b.startTime) && 
        (a.endTime == b.endTime))
        return true; 
    if(a.startTime < b.startTime) { 
      	if(a.endTime > b.endTime) 
            return true; 
        else if(a.endTime >= b.startTime) { 
            return true; 
        } else return false; 
    }
    if(b.startTime < a.startTime) { 
      	if(b.endTime > a.endTime) 
            return true; 
        else if(b.endTime >= a.startTime) { 
            return true; 
        } else return false; 
    }
    return false; 
} 

Meeting Resolve(Meeting a, Meeting b) { 
 	int startTime = a.startTime; 
    int endTime = b.endTime; 
    if(a.startTime > b.startTime) 
        startTime = b.startTime; 
	if(b.endTime < a.endTime) 
        endTime = a.endTime; 
    Meeting result = {startTime, endTime}; 
    return result; 
} 

vector<Meeting> merge(vector<Meeting> m1) { 
   	vector<Meeting> result; 
	Meeting last = m1.front(); 
    m1.erase(m1.begin()); 
    for(auto it: m1) { 
        if(HasOverLap(last, *it)) { 
           last = resolve(last, *it); 
        } else { 
        	last = *it;          
        } 
        result.emplace_back(last); 
    }
    return result; 
} 

int compare(Meeting a, Meeting b) { 
  	if(a.startTime < b.startTime) 
        return -1; 
    if(a.startTime > b.startTime) 
        return 1; 
    else return 0; 
} 

int main () {
    // run your function through some test cases here
    // remember: debugging is half the battle!
    Meeting meetArr[] = {{1,2}, {2,3}}; 
    qsort(meetArr, 2, sizeof(Meeting), compare); 
	std::vector<int> meetVec(meetArr, meetArr + sizeof(meetArr) / sizeof(meetArr[0]));
    cout << merge(meetVec);
    return 0;
}