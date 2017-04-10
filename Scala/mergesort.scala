/*
    A tail recursive implementation of MergeSort
*/

import scala.annotation.tailrec

@tailrec
def merge (l1: List[Int], l2: List[Int], mergedList: List[Int]) : List[Int] = (l1, l2) match {
    case (l1, Nil) => mergedList:::l1
    case (Nil, l2) => mergedList:::l2
    case (h1::t1, h2::t2) if h1 > h2 => merge(l1, t2, mergedList:::List(h2))
    case (h1::t1, h2::t2) if h1 <= h2 => merge(t1, l2, mergedList:::List(h1))
}

def sort (ls: List[Int]) : List[Int] = ls match {
    case Nil => Nil
    case x :: Nil => ls
    case _ => {
        val s = ls.size
        val (a, b) = ls.splitAt(s/2)
        val l1 = sort(a)
        val l2 = sort(b)
        merge(l1, l2, List())
    }
}

println("Enter the list of integers that you want to sort:")
val ls = scala.io.StdIn.readLine.split(" ").map(_.toInt).toList

println(sort(ls))
