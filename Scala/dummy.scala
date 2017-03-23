// a tail recursive function that applies the function f to every element of the list ls and returns the list retLs
def foo (ls: List[Int], f: Int => Boolean, retLs: List[Boolean]) : List[Boolean] = ls match {
    case Nil => retLs
    case h::t => foo(t, f, retLs:::List(f(h)))
}

// a function that checks if a number is even
def even (n: Int) : Boolean = {
    if (n % 2 == 0) true else false
}

val l = List(1,2,3,4,5,6)

println(foo(l, even, List()))
