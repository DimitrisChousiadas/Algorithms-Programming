/*
    Finding bridges in an undirected graph.

    The idea is to do a DFS traversal of the graph and keep the following info about each node:
        1) the state of the node (unexplored, under exploration, explored)
        2) its parent node in the DFS tree
        3) the time when the node was first visited (came under exploration)
        4) the time when the node became explored

    A bridge, then, will be an edge (u,v) such that:
        1) u is the parent of v in the DFS tree (bu definition, every bridge belongs to the DFS tree)
        2) and there are no back edges from any of the descendants of u in the tree (including v)
            to any of v's ancestors (including u).

    Also, if the root of the DFS tree has more than one children in the tree, then all the edges between the root and these children will be bridges.

    The input should be as follows:
        - First, the number of nodes in the graph (N)
        - Then, for each node:
            - the number of neighbors that the node has
            - the ids of these neighbors (from 0 to N-1)

    The output will be a list of the bridges (u, v) in the graph, where u and v are the nodes of the bridge.
*/

package main

import "fmt"

type Edge struct {
    U int
    V int
}

type Bridges []Edge

type Node struct {
    X int // the id of the node, from 0 to N-1
    Neighbors []int // the neighbors of that node
}

type Graph struct {
    N int // number of nodes in the graph
    AdjList []Node // the adjacency list that describes the graph
}

// a struct with all the information about the dfs traversal
type DFSTree struct {
    time int
    rootChildren int // how many children the root of the DFS tree
    state, parent, arrival, departure []int
    earliestReachable []int // we will use this array to check the second condition, as described above, under which an edge is a bridge
}

func min (a, b int) int {
    if (a > b) {
        return b
    } else {
        return a
    }
}

func dfs (node int, graph Graph, dfsTree DFSTree) {

    dfsTree.state[node] = 1 //under exploration
    dfsTree.time = dfsTree.time + 1
    dfsTree.arrival[node] = dfsTree.time
    dfsTree.earliestReachable[node] = dfsTree.time

    neigh := graph.AdjList[node].Neighbors
    for i := 0; i < len(neigh); i++ {
        v := neigh[i]
        if (dfsTree.state[v] == 0) {
            dfsTree.parent[v] = node
            if (node == 0) {
                dfsTree.rootChildren += 1
            }
            dfs(v, graph, dfsTree)
            dfsTree.earliestReachable[node] = min(dfsTree.earliestReachable[node], dfsTree.earliestReachable[v])
        } else {
            if (v != dfsTree.parent[node]) {
                dfsTree.earliestReachable[node] = min(dfsTree.earliestReachable[node], dfsTree.arrival[v])
            }
        }
    }

    dfsTree.state[node] = 2 //explored
    dfsTree.time += 1
    dfsTree.departure[node] = dfsTree.time

}

func dfsInit (graph Graph) DFSTree {

    var dfsTree DFSTree

    dfsTree.state = make([]int, graph.N) // 0->unexplored, 1->under exploration, 2->explored
    dfsTree.parent = make([]int, graph.N)
    dfsTree.arrival = make([]int, graph.N)
    dfsTree.departure = make([]int, graph.N)
    dfsTree.earliestReachable = make([]int, graph.N)
    dfsTree.time = 0
    dfsTree.rootChildren = 0

    for i := 0; i < graph.N; i++ {
        dfsTree.parent[i] = i
        dfsTree.state[i] = 0
    }

    // Node 0 will be the root
    for node := 0; node < graph.N; node++ {
        if (dfsTree.state[node] == 0) {
            dfs(node, graph, dfsTree)
        }
    }

    return dfsTree

}

func findBridges (graph Graph) Bridges {

    dfsTree := dfsInit(graph)

    bridges := make(Bridges, 0)

    for i := 0; i < graph.N; i++ {
        p := dfsTree.parent[i]
        if (p != i && p == 0 && dfsTree.rootChildren > 1) {
            bridges = append(bridges, Edge{U: p, V: i})
        } else {
            if (p != i && dfsTree.arrival[p] < dfsTree.earliestReachable[i]) {
                bridges = append(bridges, Edge{U: p, V: i})
            }
        }
    }

    return bridges

}

func main() {

    var n, temp int
    var node Node
    var graph Graph

    fmt.Println("Enter the number of nodes in the graph:")
    fmt.Scanf("%d", &n)

    graph = Graph{N: n, AdjList: make([]Node, n)}

    for i := 0; i < n; i++ {

        fmt.Printf("Enter the number of neighbors of the %dth node:\n", i)
        fmt.Scanf("%d", &temp)

        fmt.Printf("Enter the neighbors of the %dth node:\n", i)
        node = Node{X: i, Neighbors: make([]int, temp)}

        for j := 0; j < temp; j++ {
            fmt.Scanf("%d", &node.Neighbors[j])
        }

        graph.AdjList[i] = node
    }

    bridges := findBridges(graph)

    fmt.Println("The bridges of the graph are:")
    for i := 0; i < len(bridges); i++ {
        fmt.Printf("(%d, %d)\n", bridges[i].U, bridges[i].V)
    }

}
