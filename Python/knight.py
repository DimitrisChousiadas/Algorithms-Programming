"""
    On an NxN chessboard, a knight starts on the (1, 1) cells and we want to find out
    how many moves it needs to reach the (N, N) cell.
    The knight can move in L shape and its movement depends on two parameters a, b, such that the total
    lenght of the L movement must be a+b.
    In other words, if a knight is at position (x1, y1) then the new position (x2, y2) must satisfy one of the following:
        - |x2-x1| = a and |y2-y1| = b
        - |x2-x1| = b and |y2-y1| = a
    (of course, the new position must be within the borders of the chessboard)

    The question is to find, for each possible pair (a, b), what is the minimum number of moves
    the knight needs to reach the (N, N) cell, if it starts from the (1, 1) cell.
    If it can reach, we print the minimum number of moves it needs.
    If it can't reach it, we print -1.

    To do that, we use a FIFO queue, where we store the positions the knight has visited, as long as the number of moves it made
    to reach them, as well as a set to keep track of the positions the knight has visited.
    We initialize the queue with the entry (1,1,0), since the knight begins from the (1,1) position.
    Then, while the queue is not empty we do the following:
        - extract first entry from the queue
        - if the entry is the (N, N, l) we return l
        - otherwise, for each possible next position, and if we haven't visited it before (i.e. it is not in the set),
          we add it to the set and we add it in the queue, increasing the number of movements by one.
    If the queue empties, then the knight cannot reach the (N, N) position, in which case we return -1.

    Generally, the above algorithm is like doing a BFS on the tree of all the positions the knight can reach on the board.
    The complexity is O(#positions the knight can reach on the board) = O(N^2) in the worst case.

    The input is the integer N.
    The output is an NxN matrix, where the entry (a, b) denotes the min number of moves the knight must make to reach the (N, N) cell
    with the parameters a and b.
    Obviously, this matrix will be symmetric.
"""

import collections

def min_moves (n, a, b):

    visited = set()
    queue = collections.deque()
    queue.appendleft((0, 0, 0))

    while queue:

        x, y, l = queue.popleft()

        if x == n-1 and y == n-1:
            return l

        for (i, j) in zip([a, b], [b, a]):
            for nextX in [x + i, x - i]:
                for nextY in [y + j, y - j]:
                    if 0 <= nextX < n and 0 <= nextY < n and not (nextX, nextY) in visited:
                        visited.add((nextX, nextY))
                        queue.append((nextX, nextY, l + 1))

    return -1


n = int(input().strip())
for a in range(1,n):
    for b in range(1,n):
        print(min_moves(n, a, b), end=' ')
    print()
