/*
    Given a list of buildings on a 2D plane, the following program calculates the skyline that the buildings form.
    Each building is described by three integers (l, r, h), one for the beginning (l) of the building, one for the end (r) and one for the height (h) of it.
    The skyline is a list of pairs of two integers (x, h),  the first one being a point on the X axis and the second the height at this point.

    For example, the following buildings:
        (1, 4, 2), (3, 6, 5), (5, 7, 4)
    form the following skyline:
        (1, 2), (3, 5), (6, 4), (7, 0)

    To solve the problem, at first we sort all the points on the X axis, based on the l value.
    If two buildings begin at the same point, we first consider the higher one.
    If two buildings end at the same point, we first consider the lower one.
    If a building begins where another one ends, we first consider the former.

    Once we sort the points, we iterate over them.
    When we encounter a starting point we add it to a priority queue, that is implemented as a binary heap.
    When we encounter an end point we remove it from the heap.
    Every time we add or remove an element from the heap we check if the maximum value of it changes.
    If it does then we add in the skyline the pair (x, max), where x is the x-coordinate of the point we were considering and max is the new maximum value in the heap.
    The initial element in the heap is 0, which we use to indicate an otherwise empty heap.

    The input that the program expects from the keyboard is, first, an integer n which is the number of the buildings and, then, n triples (l, r, h), one for every building.
*/


package main

import "fmt"

type Point struct {
    X int
    Height int
    Type int // 0 for the beginning, 1 for the end of the building
}

type SkylinePoint struct {
    X int
    Height int
}

type PriorityQ []int

type Skyline []SkylinePoint


func mergePoints (p1, p2 []Point) []Point {

    n1 := len(p1)
    n2 := len(p2)

    p := make([]Point, n1+n2)

    i := 0
    j := 0

    for i+j < n1+n2 {
        switch {
        case i == n1:
            p[i+j] = p2[j]
            j++
        case j == n2:
            p[i+j] = p1[i]
            i++
        case p1[i].X < p2[j].X:
            p[i+j] = p1[i]
            i++
        case p2[j].X < p1[i].X:
            p[i+j] = p2[j]
            j++
        case p1[i].Type == 0 && p2[j].Type == 0 && p1[i].Height >= p2[j].Height:
            p[i+j] = p1[i]
            i++
        case p1[i].Type == 0 && p2[j].Type == 0 && p1[i].Height < p2[j].Height:
            p[i+j] = p2[j]
            j++
        case p1[i].Type == 1 && p2[j].Type == 1 && p1[i].Height <= p2[j].Height:
            p[i+j] = p1[i]
            i++
        case p1[i].Type == 1 && p2[j].Type == 1 && p1[i].Height > p2[j].Height:
            p[i+j] = p2[j]
            j++
        case p1[i].Type == 0 && p2[j].Type == 1:
            p[i+j] = p1[i]
            i++
        case p1[i].Type == 1 && p2[j].Type == 0:
            p[i+j] = p2[j]
            j++
        }
    }

    return p

}

func sortPoints (points []Point) []Point {

    n := len(points)

    if (n == 1) {
        return points
    }

    p1 := sortPoints(points[:n/2])
    p2 := sortPoints(points[n/2:])
    return mergePoints(p1, p2)

}

func (q PriorityQ) Swap (p, i int) PriorityQ {

    temp := q[p]
    q[p] = q[i]
    q[i] = temp
    return q

}

func (q PriorityQ) Insert (val int) PriorityQ {

    if (q[0] == 0) {
        q[0] = val
        return q
    }

    q = append(q, val)

    i := len(q)-1
    p := i/2

    for i > 0 && q[p] < q[i] {
        q = q.Swap(p, i)
        i = p
        p = (i-1)/2
    }

    return q

}

func (q PriorityQ) Combine (i int) PriorityQ {

    l := len(q)
    left := 2*i + 1
    right := 2*i + 2
    mp := i

    if (l == 1) {
        return q
    }

    if (left < l && q[left] > q[mp]) {
        mp = left
    }
    if (right < l && q[right] > q[mp]) {
        mp = right
    }

    if (mp != i) {
        q = q.Swap(i, mp)
        q = q.Combine(mp)
        return q
    } else {
        return q
    }

}

func (q PriorityQ) Delete (val int) PriorityQ {

    l := len(q)

    if (l == 1) {
        q[0] = 0
        return q
    }

    for i := 0; i < l; i++ {
        if (val == q[i]) {
            q[i] = q[l-1]
            q = q[:l-1]
            q = q.Combine(i)
            break
        }
    }

    return q

}

func findSkylinePoints (points []Point) Skyline {

    var max int
    var p Point
    var q PriorityQ

    skyline := make(Skyline, 0)

    q = append(q, 0)

    for i := 0; i < len(points); i++ {

        p = points[i]
        max = q[0]

        if (p.Type == 0) {
            q = q.Insert(p.Height)
            if (max != q[0]) {
                skyline = append(skyline, SkylinePoint{X: p.X, Height: p.Height})
            }
        } else {
            q = q.Delete(p.Height)
            if (max != q[0]) {
                skyline = append(skyline, SkylinePoint{X: p.X, Height: q[0]})
            }
        }
    }

    return skyline

}


func main() {

    var n, l, r, h int
    //n is the  number of buildings
    var points []Point

    fmt.Println("Enter the number of the buildings:")
    fmt.Scanf("%d", &n)
    points = make([]Point, 2*n)

    fmt.Println("Enter the coordinates and heights of the buildings:")
    for i := 0; i < n; i++ {
        fmt.Scanf("%d %d %d", &l, &r, &h)

        points[2*i].X = l
        points[2*i].Height = h
        points[2*i].Type = 0

        points[2*i+1].X = r
        points[2*i+1].Height = h
        points[2*i+1].Type = 1
    }

    points = sortPoints(points)
    /*for i := 0; i < 2*n; i++ {
        fmt.Printf("%d %d %d", points[i].X, points[i].Height, points[i].Type)
        fmt.Println()
    }*/

    skyline := findSkylinePoints(points)

    fmt.Println()
    fmt.Println("The skyline points are:")
    for i := 0; i < len(skyline); i++ {
        fmt.Printf("%d %d", skyline[i].X, skyline[i].Height)
        fmt.Println()
    }

}
