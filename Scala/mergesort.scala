/*
    A tail recursive implementation of MergeSort
*/

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

val ls = List(10, 23, 12, 4, 0, 0, 56, 21)

println(sort(ls))
