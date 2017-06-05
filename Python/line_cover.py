# Consider the line of positive integers
# Given a starting and an ending point on the line, as well as N intervals of positive integers,
# we want to find the minimum number of intervals that we have to use in order to cover the line segment
# We are interested in covering only the integer points.
# Example:
#   - the starting point is 5 and the ending point is 10
#   - the intervals are the following: (5, 7), (6,9), (8, 10)
#   We need, then, two intervals to cover the 5-10 segment.
#   Specifically, we can achieve this by using the first and the third interval.
# Example:
#   - the starting point is 5 and the ending point is 10
#   - the intervals are the following: (5, 7), (6,9), (8, 9)
#   In that case, we cannot cover the line segment
# Example:
#   - the starting point is 1 and the ending point is 10
#   - the intervals are the following: (1, 3), (1, 2), (3, 6), (5, 8), (4, 5), (6, 10)
#   We need, then, three intervals to cover the 5-10 segment.
#   Specifically, we can achieve this by using the intervals (1, 3), (3, 6) and (6, 10)
#   We can only achieve it with the intervals (1, 3), (4, 5) and (6, 10)
#
# To solve the problem, we first sort the intervals in ascending order of their starting points.
# After that, we traverse the ordered list once, keeping track of the furthest point that we have covered sofar.
# To cover new points, we keep traversing until we find an interval with a starting point greater than or equal to sofar + 2.
# Then, we set sofar to be the furthest ending point that we encountered.
# If the new sofar equals the old one, then we cannot cover the line segment and we return.
# Else, we increase the interval counter by one.
# If sofar >= ending point of the segment, then we have found the solution.
# The initial values of the counter is 0 and of the sofar is the start of the segment - 1.
# The time complexity of the algorithm is O(nlogn), since we sort the intervals.



"""
O(n^2)

def furthest_after_sofar (sofar):
    furthest = 0
    for i in intervals:
        if i[0] <= sofar + 1 and i[1] > max(sofar, furthest):
            furthest = i[1]
    return furthest

def line_cover ():
    sofar = start - 1
    counter = 0
    while True:
        if sofar >= end:
            print("The line segment needs", counter, "intervals to be covered")
            break
        sofar = furthest_after_sofar(sofar)
        if not sofar:
            print("The line segment cannot be covered")
            break
        counter += 1

n = int(input())
start, end = map(int, input().split())
intervals = []

for _ in range(n):
    s, e = list(map(int, input().split()))
    intervals.append((s, e))

line_cover()
"""

# O(nlogn)

def line_cover ():
    sofar = start - 1
    counter = 0
    i = 0
    while True:

        if sofar >= end:
            print("The line segment needs", counter, "intervals to be covered")
            break

        temp = sofar
        while i < n and intervals[i][0] < sofar + 2:
            temp = max(temp, intervals[i][1])
            i += 1

        if temp > sofar:
            sofar = temp
            counter += 1
        else:
            print("The line segment cannot be covered")
            break

t = int(input())
for _ in range(t):
    n = int(input())
    start, end = map(int, input().split())
    intervals = []

    for _ in range(n):
        s, e = list(map(int, input().split()))
        intervals.append((s, e))

    intervals.sort(key = lambda i: i[0])

    line_cover()
