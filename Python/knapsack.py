
# integer knapsack problem with dynamic programming
def knapsack (val, wt, capacity):

    # val: list of the values of the items
    # wt: list of weights of the items
    # capacity: capacity of the knapsack

    num_items = len(val)
    total_value = []
    # an array with dimensions num_items x capacity that we will use to store the results of the subproblems

    # we will initialize the first line of the array that correspods to the first item in the list
    total_value.append([])
    for w in range(capacity+1):
        if w < wt[0]:
            total_value[0].append(0)
        else:
            total_value[0].append(val[0])

    # each column w of the array corresponds to a knapsack of capacity w
    # an item i with weight wt[i], if it fits in the knapsack of size w, will be included if:
    #    val[i] + total_value[i-1][w-wt[i]] > total_value[i-1][w]
    for i in range(1,num_items):
        for w in range(capacity+1):
            if w == 0:
                total_value.append([0])
            elif w < wt[i]:
                total_value[i].append(total_value[i-1][w])
            else:
                v = max(val[i] + total_value[i-1][w-wt[i]], total_value[i-1][w])
                total_value[i].append(v)

    return total_value[num_items-1][capacity]



val = [int(x) for x in input().split()]
wt = [int(x) for x in input().split()]
capacity = int(input())
# input should be given like this:
#   100 120 90 60 150 140 30 90 110 60
#   6 1 12 7 10 8 3 9 14 5
#   35

print("The maximum value that can be included in the knapsack is: " + str(knapsack(val, wt, capacity)))
