/*
    Given a string, the following program determines whether the paranthesis
    in the string are balanced.

    Examples of strings with balanced paranthesis:
    - helloworld
    - h(e)ll((wor)ld)
    - ()helloworld(())

    Examples of string with unbalanced parenthesis:
    - (helloworld()
    - )()(
*/

import scala.annotation.tailrec

object BalancedParenthesis extends App {

    def isBalanced(chars: List[Char]): Boolean = {
        @tailrec
        def leftToSee (chars: List[Char], count: Int) : Boolean = {
            if (count < 0 || chars.isEmpty) count == 0
            else {
                if (chars.head == '(') leftToSee(chars.tail, count+1)
                else if (chars.head == ')') leftToSee(chars.tail, count-1)
                else leftToSee(chars.tail, count)
            }
        }
        leftToSee(chars, 0)
    }

    println("Enter the input string:")
    val charLs = scala.io.StdIn.readLine.toList // the list of characters in the input string

    if (isBalanced(charLs)) println("The paranthesis in the string are balanced!")
    else println("The paranthesis in the string are not balanced!")

}
