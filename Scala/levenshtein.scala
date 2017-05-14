// Levenshtein Distance
// Given two strings, we want to find the minimum number of operations that we need to perform to get one from the other.
// The allowed operations are substituting a character for another or adding a new character in the string.

object LevenshteinDistance extends App {

    def min3 (a: Int, b: Int, c: Int) : Int = {
        if (a < b && a < c) a
        else if (b < a && b < c) b
        else c
    }

    def min2 (a: Int, b: Int) : Int = {
        if (a < b) a
        else b
    }

    def levenshteinRecursive (s1: List[Char], s2: List[Char]) : Int = (s1, s2) match {
        case (Nil, _) => s2.length
        case (_, Nil) => s1.length
        case (h1::t1, h2::t2) =>
            if (h1 == h2) {
                min3(levenshteinRecursive(t1, t2), levenshteinRecursive(t1, s2) + 1, levenshteinRecursive(s1, t2) + 1)
            } else {
                min2(levenshteinRecursive(s1, t2) + 1, levenshteinRecursive(t1, s2) + 1)
            }
    }

    def levenshteinDynamic (s1: Array[Char], s2: Array[Char]) : Int = {
        val l1 = s1.length
        val l2 = s2.length
        var arr = new Array[Array[Int]](l1+1)
        for (i <- 0 to l1) arr(i) = new Array[Int](l2+1)
        arr(0) = (for (i <- 0 to l2) yield i).toArray
        for (i <- 1 to l1) {
            arr(i) = new Array[Int](l2+1)
            arr(i)(0) = i
            for (j <- 1 to l2) {
                if (s1(i-1) == s2(j-1)) {
                    arr(i)(j) = min3(arr(i-1)(j-1), arr(i-1)(j) + 1, arr(i)(j-1) + 1)
                } else {
                    arr(i)(j) = min2(arr(i-1)(j) + 1, arr(i)(j-1) + 1)
                }
            }
        }
        arr(l1)(l2)
    }

    println("Enter the first input string:")
    val s1 = scala.io.StdIn.readLine.toList // the list of characters in the first input string
    println("Enter the second input string:")
    val s2 = scala.io.StdIn.readLine.toList // the list of characters in the second input string
    println("The Levenshtein distance between the strings computed recursively is: " + levenshteinRecursive(s1, s2))
    println("The Levenshtein distance between the strings computed with dynamic programming is: " + levenshteinDynamic(s1.toArray, s2.toArray))

}
