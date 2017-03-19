/*
    A program that reads a positive integer i from the keyboard and prints the ith fibonacci number.
    The number is calculated with dynamic programming.
*/

package main

import "fmt"

func fibonacci (num int) {

	fibSeq := make([]int, num+1)

	fibSeq[0] = 0
	fibSeq[1] = 1

	for i := 2; i <= num; i++ {
		fibSeq[i] = fibSeq[i-1] + fibSeq[i-2]
	}

	fmt.Printf("The %dth Fibonacci number is: %d\n", num, fibSeq[num])

}

func main() {

	var num int

	fmt.Print("Enter a number: ")
	fmt.Scanf("%d", &num)

	fibonacci(num)

}
