// Factorial, with a nested, tail recursive function

import scala.annotation.tailrec

def factorial (n: Int) : Int = {

    @tailrec
    def tailFact (n: Int, acc: Int) : Int = n match {
        case 0 => acc
        case 1 => acc
        case _ => tailFact(n-1, n*acc)
    }

    tailFact(n, 1)
}

println("Enter a positive integer:")
val n = scala.io.StdIn.readInt()
println("The factorial of the number is: " + factorial(n))
