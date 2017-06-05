"""
    On an NxM grid there are K row intervals that are occupied.
    Specifically, a row interval (r, c1, c2) means that the cells in row r and between
    columns c1 and c2 (both included) are occupied.
    These K intervals may overlap with each other.
    The question is how many cells in the grid are free.

    To find that out, we use a dictionary that maps a row index to a list of the intervals that exist in that row.
    Concretely, for each interval (r, c1, c2) we create two entries in the respective list in the dictionary:
        - the entry (c1, "start"), which means that on the column c1 an interval starts
        - the entry (c2, "end"), which means that on the column c2 an interval ends
    Then, for each key (i.e. row) in the dictionary, we sort the value (i.e. the list) in ascending order of the column value
    and, to break the ties, we the "start" of an interval comes before the "end" of an interval.
    Then, by traversing each list once, we can count how many cells in that row are occupied and substract the total sum
    from the number of cells in the grid, i.e. NxM.

    The time complexity of the algorithm is O(K*logK), since we are reading the input (O(K)), accessing and updating the dictionary
    (O(1) on average for each operation) and sorting the 2*K entries, which takes O(KlogK) time.
"""

row_intervals = {}

n, m, k = map(int, input().strip().split())

for _ in range(k):
    row, c1, c2 = map(int, input().strip().split())
    if row in row_intervals:
        new = row_intervals[row]
        new.append((c1, "start"))
        new.append((c2, "end"))
        row_intervals[row] = new
    else:
        row_intervals[row] = [(c1, "start"), (c2, "end")]

occupied = 0
for row in row_intervals:
    intervals = row_intervals[row]
    intervals.sort( key = lambda el : (el[0], el[1] == "end") )
    starts = 0
    for (c, t) in intervals:
        if t == "start" and starts == 0:
            starts = 1
            c_prev = c
        elif t == "start":
            starts += 1
        elif t == "end" and starts == 1:
            occupied += c - c_prev + 1
            starts = 0
        elif t == "end":
            starts -= 1

print(n*m - occupied)
