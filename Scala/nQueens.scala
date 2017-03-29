/*
    The problem is to place N queens on a chess board of size NxN,
    so that no queen is attacked.
    We know that there is always a solution to the problem,
    except for N<4
*/

case class Position (x: Int, y: Int)

// returns true if two queens at positions p1 and p2 threaten each other
def threat (p1: Position, p2: Position) : Boolean = {

    def threatRow (p1: Position, p2: Position) : Boolean = {
        if (p1.x == p2.x) true else false
    }

    def threatColumn (p1: Position, p2: Position) : Boolean = {
        if (p1.y == p2.y) true else false
    }

    def threatDiag (p1: Position, p2: Position) : Boolean = {
        if ((p1.x - p1.y) == (p2.x - p2.y) || (p1.x + p1.y) == (p2.y + p2.x)) true
        else false
    }

    return (threatRow(p1,p2) || threatColumn(p1, p2) || threatDiag(p1, p2))
}

// Returns false if placing a queen at position p is possible, given that there
// are queens at the positions in the list posLs.
// Returns true if it is not possible, i.e. if there is a conflict
def conflict (p: Position, pLs: List[Position]) : Boolean = pLs match {
    case Nil => false
    case h::t => threat(p, h) || conflict(p, t)
}

// Given the positions in the posLs list, where there are queens,
// we want to find the next safe, that is without conflicts, position
// on the board, starting from the position pos, where we can place a queen.
// Starting from pos means that we cannot place the queen at any previous position.
def safePosition (size: Int, pos: Position, posLs: List[Position]) : Position = {
    val i = pos.x
    val j = pos.y
    if (i == size && j == size) {
        if (conflict(pos, posLs)) return Position(0,0)
        else return pos
    }
    else {
        if (j == size) {
            if (conflict(pos, posLs)) return safePosition(size, Position(i+1, 1), posLs)
            else return pos
        } else {
            if (conflict(pos, posLs)) return safePosition(size, Position(i, j+1), posLs)
            else return pos
        }
    }

}

// It returns the next position of pos on the board
def nextPos (pos: Position, size: Int) : Position = {
    if (pos.y == size) Position(pos.x+1, 1)
    else Position(pos.x, pos.y+1)
}

// The following function places the N queens on the board.
// size is the size of the board, i.e. the parameter N.
// posLs is the list of the positions on the board already occupied by a queen.
// nextToTry is the next position of the position that we already tried to
// place the i-th queen, with the same posLs, and we failed.
// The function returns the N positions where we can place the N queens.
def fillTheBoard (size: Int, nextToTry: Position, posLs: List[Position]) : List[Position] = {
    if (posLs.length == size) posLs
    else {
        val pos = safePosition(size, nextToTry, posLs)
        if (pos.x == 0 && pos.y == 0) {
            val h::t = posLs
            fillTheBoard(size, nextPos(h, size), t)
        }
        else {
            fillTheBoard(size, Position(1,1), List(pos):::posLs)
        }
    }
}

// The parameter N is given from the keyboard
println("Enter the size of the chess board N:")
val n = scala.io.StdIn.readInt()
if (n < 4) println("There is no solution with N < 4")
else {
    val l = fillTheBoard(n, Position(1,1), List())
    println("The positions of the N queens are:")
    for (pos <- l) println(pos.x + " " + pos.y)
}
