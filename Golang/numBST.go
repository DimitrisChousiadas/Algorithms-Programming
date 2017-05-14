/*
    Given a positive integer N, we want to compute how many different Binary Search Trees are there with N nodes.
    Concretely, each node of the tree has a value, which is an integer from 1 to N, a left child and a right child.
    The left child is, again, a BST, and all the values in it are smaller than the value of the node.
    The right child is a BST whose values are all greater than the values of the node.
    The leaves of the tree only have values.
    We want to compute how many BSTs are there with N nodes, that have all values 1 to N.

    A first solution to the problem is with dynamic programming. Specifically, let k be the value of the root node of the tree.
    Then, the left subtree has k-1 nodes and all the values 1 to k-1.
    The right subtree, on the other hand, has N-k nodes, values k+1 to N.
    If we define C(N) the number of BSTs with N nodes, as described above, then there are C(k-1) BSTs with k-1 nodes and C(N-k) BSTs with N-k nodes.
    It doesn't matter that the values of the right subtree are k+1 to N, and not 1 to N-k, since it's just the ordering of the values that matters
    and not the absolute values.
    So, there are C(k-1)*C(N-k) BSTs, where the value of the root node is k, since each one of the C(k-1) left subtrees can be combined with each one of the
    C(N-k) right subtrees.
    As a result, we can compute C(N) as sum(C(k-1)*C(N-k)), for all k = 1,...,N
    The base of the recursion is C(0) = 1 and C(1) = 1, since there is only one BST with one node.
    This algorithm is implemented by the countBSTs function in O(n^2) time.

    A second, and more efficient solution, is to use the Catalan number formula, which solves the same problem.
    The nth Catalan number is given by Cn = (2n)! / ((n+1)!n!)
    The following function catalan computes the nth Catalan number and solves the problem in O(n) time.
*/

package main

import "fmt"

func binomialCoeff (n int, k int) int64 {

    if (k > n-k) {
        k = n-k
    }

    var res int64
    res = 1
    for i := 0; i < k; i++ {
        res *= int64(n-i)
        res /= int64(i+1)
    }

    return res
}

func catalan (n int) int64 {
    return binomialCoeff(2*n, n)/int64(n+1)
}

func countBSTs (n int) int64 {

    arr := make([]int64, n+1)
    arr[0] = 1
    arr[1] = 1

    for i := 2; i <= n; i++ {
        arr[i] = 0
        for k := 1; k <= i; k ++ {
            arr[i] += arr[k-1]*arr[i-k]
        }
    }

    return arr[n]

}

func main () {

    var n int
    fmt.Println("Enter the number of nodes in the bst:")
    fmt.Scanf("%d", &n)

    res := countBSTs(n)
    fmt.Printf("The number of binary search trees with nodes 1,2,..,N, computed with dynamic programming in O(n^2), is %d \n", res)
    fmt.Printf("The number of binary search trees with nodes 1,2,..,N, computed in O(n) using the Catalan Numbers formula, is %d \n", catalan(n))

}
