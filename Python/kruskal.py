# A program that finds the MST (minimum spanning tree) of a graph using Kruskal's algorithm.
# The input id, first, a number N which is the number of nodes.
# Then, N lines follow, each of which is a row of the adjacency matrix of the graph.
# First, we sort the edges of the graph with quicksort.
# Then, we iterate over the sorted edges, adding an edge to the MST, if no circle is formed.
# We use a Union-Find structure to look for circles.
# For the Union-Find we use the path compression and the weighted union heuristics.

from collections import namedtuple
from random import randint

Edge = namedtuple("Edge", "x y w")

# a function that checks if the input is correct
def check_input (adj_matrix):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i,n):
            if i == j and adj_matrix[i][j] != 0:
                return False
            if adj_matrix[i][j] != adj_matrix[j][i]:
                return False
    return True

# a function that selects a random pivot and partitions the edges array
# between the left and the right position, using that pivot.
def partition (edges, left, right):
    pivot = edges[randint(left, right)].w
    i = left
    j = right
    while True:
        while(i <= right and edges[i].w <= pivot):
            i += 1
        while(j >= left and edges[j].w > pivot):
            j -= 1
        if i < j:
            temp = edges[i]
            edges[i] = edges[j]
            edges[j] = temp
            i += 1
            j -= 1
        else:
            # if the pivot was the minimum of the array
            # we increase j by 1 so that some partitioning does happen
            if j == left:
                j += 1
            # if the pivot was the maximum of the array
            # we decrease j by 1, so that some partitioning does happen
            if j == right:
                j -= 1
            return j

def quick_sort (edges, left, right):
    if not edges:
        return
    if left >= right:
        return
    q = partition(edges, left, right)
    quick_sort(edges, left, q)
    quick_sort(edges, q+1, right)
    return

def sort_edges (adj_matrix):
    n = len(adj_matrix)
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            if adj_matrix[i][j] != 0:
                edges.append(Edge(i, j, adj_matrix[i][j]))
    quick_sort(edges, 0, n-1)
    return edges

# finding the group where x belongs, implementing the path compression at the same time
def find (group, x):
    if x != group[x]["parent"]:
        group[x]["parent"] = find(group, group[x]["parent"])
    return group[x]["parent"]

# doing the union of two groups
# with x and y being the roots for each group.
def union (group, x, y):
    if x == y:
        return
    if group[x]["length"] > group[y]["length"]:
        group[y]["parent"] = x
    elif group[x]["length"] < group[y]["length"]:
        group[x]["parent"] = y
    else:
        group[y]["parent"] = x
        group[x]["length"] += 1

# Kruskal's algorithm
def kruskal (edges, group):
    mst = []
    i = 0
    while len(mst) < len(group)-1 and i < len(edges):
        x = edges[i].x
        y = edges[i].y
        p1 = find(group, x)
        p2 = find(group, y)
        if p1 != p2:
            mst.append(edges[i])
            union(group, p1, p2)
        i += 1
    return mst

if __name__ == "__main__":
    print("Enter the number of nodes in the graph:")
    n = int(input())    # number of nodes in the graph
    adj_matrix = []     # the adjacency matrix of the graph
    print("Enter the adjacency matrix of the graph:")
    for i in range(n):
        adj_matrix.append([int(j) for j in input().split()])

    flag = check_input(adj_matrix)
    if not flag:
        print("The input is wrong!")
    else:
        edges = sort_edges(adj_matrix)
        group = []
        for i in range(n):
            group.append({"parent": i, "length": 1})
        mst = kruskal(edges, group)
        total_weight = 0
        print("The minimum spanning tree has the following edges:")
        for i in range(len(mst)):
            print("(" + str(mst[i].x) + "," + str(mst[i].y) + ")")
            total_weight += mst[i].w
        print("The total weight of the mst is: ", total_weight)
