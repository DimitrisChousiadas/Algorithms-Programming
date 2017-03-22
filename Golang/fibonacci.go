/*
    A program that reads a positive integer i from the keyboard and prints the list of the fibonacci numbers until the ith one.
*/

package main

import "fmt"

func fibonacci (num int) {

	fibSeq := make([]int, num+1)

	fibSeq[0] = 0
	fmt.Printf("The %dst Fibonacci number is: %d\n", 1, 0)
	fibSeq[1] = 1
	fmt.Printf("The %dnd Fibonacci number is: %d\n", 2, 1)

	for i := 2; i < num; i++ {
		fibSeq[i] = fibSeq[i-1] + fibSeq[i-2]
		fmt.Printf("The %dth Fibonacci number is: %d\n", i+1, fibSeq[i])
	}

}

func main() {

	var num int

	fmt.Print("Enter a number: ")
	fmt.Scanf("%d", &num)

	fibonacci(num)

}
