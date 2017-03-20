/*
    Given a 9x9 sudoku matrix from the keyboard, the following code determines whether or not the puzzle is solvable.
    An empty cell is has 0.
    We use backtracking to solve the problem.
*/

package main

import "fmt"

const size = 9
const n = 3
var sudoku [size][size] int

func isSolvable () bool {

    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {

            if (sudoku[i][j] == 0) {

                for test := 1; test <= 9; test++ {

                    // we assume there is going to be some conflict with the test value we picked
                    conflict := false

                    // checking for a conflict in the same row
                    for k := 0; k < size; k++ {
                        if (sudoku[i][k] == test) {
                            conflict = true
                            break
                        }
                    }

                    // if there was a conflict we continue with the next test value
                    if (conflict) {
                        continue
                    }

                    // checking for a conflict in the same column
                    for k := 0; k < size; k++ {
                        if (sudoku[k][j] == test) {
                            conflict = true
                            break
                        }
                    }

                    if (conflict) {
                        continue
                    }

                    // checking for a conflict in the same block
                    blockX := i / n
                    blockY := j / n
                    for x := 0; x < n; x++ {
                        for y := 0; y < n; y++ {
                            if (sudoku[n*blockX+x][n*blockY+y] == test) {
                                conflict = true
                                break
                            }
                        }
                    }

                    if (conflict) {
                        continue
                    } else {
                        // there was no conflict, so we can try the test value
                        sudoku[i][j] = test
                        if (isSolvable()) {
                            return true
                        } else {
                            // if the test was unsuccessfull we continue with the next test value
                            sudoku[i][j] = 0
                            continue
                        }
                    }

                }

                // if all numbers were tried in the position then the puzzle is not solvable
                return false

            }

        }
    }

    // the puzzle is solvable if it is full
    return true

}

func main() {

    // the program expects 9x9 = 81 integers from the keyboard
    fmt.Println("Enter the semi-completed sudoku puzzle:")
    for i := 0; i < size; i++ {
            for j := 0; j < size; j++ {
                fmt.Scanf("%d", &sudoku[i][j])
            }
    }

    fmt.Println()
    /*for i := 0; i < size; i++ {
            for j := 0; j < size; j++ {
                fmt.Printf("%d ", sudoku[i][j])
            }
            fmt.Println()
    }*/

    if (isSolvable()) {
        fmt.Println("The puzzle is solvable. The solution is: ")
        fmt.Println()
        for i := 0; i < size; i++ {
                for j := 0; j < size; j++ {
                    fmt.Printf("%d ", sudoku[i][j])
                }
                fmt.Println()
        }
    } else {
        fmt.Println("The puzzle is not solvable!")
    }

}
