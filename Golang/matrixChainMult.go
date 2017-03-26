/*
    Matrix Chain Multiplication:

    Given some matrices, we want to find the minimum cost of multiplying them, provided that
    the multiplication is possible.

    For example, if A, B, C are three matrices, with dimensions (2,4), (4,7) and (7,3) respectively,
    then we can multiply them in two ways:
        1) (AB)C, which has a cost of 2x4x7 + 2x7x3 = 98
        2) A(BC), with a cost of 2x4x3 + 4x7x3 = 108
    So, the best way to multiply them is the first one.

    Generally, if we have N matrices, from 1 to N, the minimum cost of multiplying all the matrices
    between the i-th and j-th matrix is (including i and j):
        - 0, if i=j
        - C(i,j) = min{ C(i,k) + C(k+1,j) + Ni*Mk*Mj }, for i<=k<j, where Ni, Mk, Mj the respective dimensions of
        the i-th, k-th and j-th matrix.
    What we want, in the end, is the cost C(1,N).

    The following program uses the above recursion and finds, with dynamic programming,
    the minimum cost of multiplying the matrices.

    The input to the program is from the keyboard, as follows:
        - First, an integer N which is the number of the matrices
        - Then, 2*N integers, that are the dimensions of the matrices
    The output will be the minimum cost of the multiplication, or a message saying that
    the multiplication is not possible, if the dimensions of any two consecutive matrices don't match.
*/

package main

import "fmt"

type Matrix struct {
    N int
    M int
}

const LEN int = 100

func multiplicationCost (len int, matrices []Matrix) int {

    var costMatrix [LEN][LEN]int
    var i, j, k, x, y, min, temp int

    for x = 0; x < len; x++ {
        for y = 0; y < len-x; y++ {

            i = y
            j = i + x
            if (i == j) {
                costMatrix[i][j] = 0
            } else {
                min = costMatrix[i+1][j] + (matrices[i].N)*(matrices[i].M)*(matrices[j].M)
                for k = i+1; k < j; k++ {
                    temp = costMatrix[i][k] + costMatrix[k+1][j] + (matrices[i].N)*(matrices[k].M)*(matrices[j].M)
                    if (temp < min) {
                        min = temp
                    }
                }
                costMatrix[i][j] = min
            }

        }
    }

    return costMatrix[0][len-1]

}

func goodForMultiplication (len int, matrices []Matrix) bool {

    for i := 1; i < len; i++ {
        if (matrices[i].N != matrices[i-1].M) {
            return false
        }
    }

    return true

}

func main() {

    var len, n, m int
    var matrices []Matrix

    fmt.Println("Enter the lenber of matrices:")
    fmt.Scanf("%d", &len)
    matrices = make([]Matrix, len)
    fmt.Println("Enter the size of each matrix:")
    for i := 0; i < len; i++ {
        fmt.Scanf("%d", &n)
        fmt.Scanf("%d", &m)
        matrices[i] = Matrix{N: n, M: m}
    }

    if (goodForMultiplication(len, matrices)) {
        fmt.Printf("The minimum multiplication cost of the matrices is: %d\n", multiplicationCost(len, matrices))
    } else {
        fmt.Println("Multiplication is not allowed between the matrices")
    }

}
