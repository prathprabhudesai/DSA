''' this is an implementation of graph using adj matrix and adj list'''
import sll as l
import queue as q
import stack as s

# to implement the adj matrix graph, we will generate a matrix of V x V
# we can address all posiible edges
class GRAPH_ADJ_MAT:
    def __init__(self, V, DIRECTED=False):
        self.V = V
        self.g = V*[None]
        for i in range(V):
            self.g[i] = V*[None]
        self.directed = DIRECTED
        
    def add_edge(self, V1, V2, w=None):
        if w is None: w = 1
        self.g[V1][V2] = w
        if (self.directed is False):
            self.g[V2][V1] = w
    
    def printg(self):
        print("\nGraph: \n")
        for i in range(self.V):
            print("| "),
            for j in range(self.V):
                print(self.g[i][j]),
            print(" |\n")

# the adjacency list works in a different way
# we will create a linked list for each node
# we can use the same api's we have create for the list or
# we can write the similar apis
# let's use the sll apis
class GRAPH_ADJ_LIST:
    def __init__(self, V, DIRECTED=False, WEIGHTED=False):
        self.V = V
        self.g = [None]*V
        for i in range(V):
            # initialize the linked list for each
            self.g[i] = l.SLL()
        self.directed = DIRECTED
        self.weighted = WEIGHTED
        if (WEIGHTED):
            self.w = V*[None]
            for i in range(V):
                # creating a hash table or if you use modified linked list
                # add weight in the node for linked list
                self.w[i] = {}

    def add_edge(self, V1, V2, w=None):
        if ((w is None) and (self.weighted is True)): w = 1
        self.g[V1].insert(V2)
        if (self.directed is False):
            self.g[V2].insert(V1)
        if (self.weighted is True):
            self.w[V1][V2] = w
            if (self.directed is False):
                self.w[V2][V1] = w
            
    def printg(self):
        print("\nGraph: \n")
        for i in range(self.V):
            print("%d -> "%i),
            self.g[i].printl()

    def BFS(self, V=None):
        # if V is not provided start the BFS from 0th node
        if V is None: V = 0
        print("\nBFS from %d: "%(V)),
        # to implement this we need queue
        bfs_queue = q.QUEUE()
        # also the visited array or dictionary basically O(1) lookup
        visited = {}

        bfs_queue.enqueue(V)
        visited[V] = True
        while(bfs_queue.size > 0):
            d = bfs_queue.dequeue().value
            curr = self.g[d].head
            while(curr is not None):
                if (visited.get(curr.value) is None):
                    bfs_queue.enqueue(curr.value)
                    visited[curr.value] = True
                curr = curr.next
            print(d),

    def DFS(self, V=None):
        # if V is not provided start the BFS from 0th node
        if V is None: V = 0
        print("\nDFS from %d: "%(V)),
        # to implement this we need stack
        dfs_stack = s.STACK()
        # also the visited array or dictionary basically O(1) lookup
        visited = {}
        dfs_stack.push(V)
        while(dfs_stack.size > 0):
            p = dfs_stack.pop().value
            if visited.get(p) is None:
                visited[p]= True
                print(p),
                curr = self.g[p].head
                while(curr is not None):
                    dfs_stack.push(curr.value)
                    curr = curr.next

    def DFS_utility_function(self, v, visited):
        visited[v] = True
        curr = self.g[v].head
        while(curr is not None):
            if visited.get(curr.value) is None:
                self.DFS_utility_function(curr.value, visited)
            curr = curr.next

                    
    def DFS_using_call_stack(self, V=None):
        # if V is not provided start the BFS from 0th node
        if V is None:
            print("\nDFS using call stack: ")
        else:
            print("\nDFS from %d suing call stack: "%(V)),
        # to implement this we need stack - so we will use call stack (recursion)
        visited = {}
        # so the graph might be disconnected
        # to handle that we should call DFS_utility_function
        # for all the other nodes if they are not visited
        if V is None:
            for i in range(self.V):
                if visited.get(i) is None:
                    self.DFS_utility_function(i, visited)
        else:
            self.DFS_utility_function(V, visited)


    def find_a_mother_vertex(self):
        # A mother vertex in a graph G = (V,E) is a vertex v such that
        # all other vertices in G can be reached by a path from v
        # in undirected connected graph, it will be any node
        # any disconnected graph - no mother node
        # directed connected graph - we have to find
        # naive approach would be to do DFS/BFS and check if we have visited all the nodes
        # that will be O(V(E + V))
        # we will use komraju's algorithm

        visited = {}
        # to store last visted vertex
        v = 0

        # from every node run DFS and store the last visited node
        for i in range(self.V):
            if visited.get(i) is None:
                self.DFS_utility_function(i, visited)
                v = i

        # now run DFS from this node
        visited = {}
        self.DFS_utility_function(v, visited)

        # now ideally if mother node is present then visited should have all the nodes
        if len(visited.keys()) == self.V:
            return v
        else:
            return -1


    def DFS_for_TC(self, s, v, tc):
        # since we are passing the same node, mark s to v reachability
        tc[s][v] = 1

        # find all vertices reachable through v
        curr = self.g[v].head
        while(curr is not None):
            if tc[s][curr.value] == 0:
                self.DFS_for_TC(s, curr.value, tc)
            curr = curr.next
        
    def transitive_closure(self):
        # Given a directed graph, find out if a vertex v is reachable from another vertex u
        # for all vertex pairs (u, v) in the given graph.
        # that is there is a path from vertex u to vertex v
        # the reachability matrix is called as the transitive closure
        trans_closure = [0]*self.V
        for i in range(self.V):
            trans_closure[i] = [0]*self.V
        for i in range(self.V):
            self.DFS_for_TC(i, i, trans_closure)
        print("\nTransitive Closure: ")
        for i in range(self.V):
            print(trans_closure[i])

    def count_paths(self, v, d, visited, path_count):
        visited[v] = True
        if (v == d):
            path_count[0] += 1
        else:
            curr = self.g[v].head
            while (curr is not None):
                if (visited[curr.value] == False):
                    self.count_paths(curr.value, d, visited, path_count)
                curr = curr.next
        visited[v] = False

    def find_all_possible_paths_between_two_nodes(self, s, d):
        # These paths don't contain a cycle, the simple enough reason is that a cylce
        # contain infinite number of paths and hence they create problem
        # The problem can be solved using backtracking, that is we take a path and start walking it,
        # if it leads us to the destination vertex then we count the path and backtrack to take
        # another path. If the path doesn't leads us to the destination vertex, we discard the path.
        visited = self.V * [False]
        path_count = [0] # array remains the same if we call multiple functions on it
        self.count_paths(s, d, visited, path_count)
        return path_count[0]

    def transpose(self):
        gt = GRAPH_ADJ_LIST(self.V, self.directed)
        for i in range(self.V):
            curr = self.g[i].head
            while(curr):
                gt.add_edge(curr.value, i)
                curr = curr.next
        gt.printg()

    def is_cyclic_directed(self, i, visited, recursion_stack):
        visited[i] = True
        recursion_stack[i] = True
        curr = self.g[i].head
        while(curr):
            if (visited[curr.value] == False):
                if self.is_cyclic_directed(curr.value, visited, recursion_stack) == True:
                    return True
            elif recursion_stack[curr.value] == True:
                return True
            curr = curr.next
        recursion_stack[i] = False
        return False

    def detect_a_cycle_DIRECTED(self):
        visited = [False]*self.V
        recursion_stack = [0]*self.V
        for i in range(self.V):
            if (not visited[i]):
                if self.is_cyclic_directed(i, visited, recursion_stack) == True:
                    return True
        return False


    def is_cyclic_undirected(self, i, visited, parent):
        visited[i] = True
        curr = self.g[i].head
        while(curr):
            if (not visited[curr.value]):
                if self.is_cyclic_undirected(curr.value, visited, parent) == True:
                    return True
            elif curr.value != parent:
                return True
            curr = curr.next
        return False
    
    def detect_a_cycle_UNDIRECTED(self):
        visited = [False]*self.V
        parent = -1
        for i in range(self.V):
            if (not visited[i]):
                if self.is_cyclic_undirected(i, visited, parent) == True:
                    return True
        return False

    def detect_a_cycle(self):
        if self.directed:
            return self.detect_a_cycle_DIRECTED()
        else:
            return self.detect_a_cycle_UNDIRECTED()
        
# we will implement most of the functions with adjacency list as
# most of the multi node graphs will be implemented in real life
# with adjacency list
            
if __name__ == "__main__":
    g = GRAPH_ADJ_LIST(5, DIRECTED=False)
    g.add_edge(1, 0) 
    g.add_edge(0, 2) 
    g.add_edge(2, 0) 
    g.add_edge(0, 3) 
    g.add_edge(3, 4)  
    g.printg()
    #g.BFS(2)
    #g.DFS(2)
    #g.DFS_using_call_stack()
    #print("Mother vertes for this graph is ", g.find_a_mother_vertex())
    #g.transitive_closure()
    #print("total number of paths between 2 and 3 are ", g.find_all_possible_paths_between_two_nodes(2, 3))
    #g.transpose()
    print(g.detect_a_cycle())
