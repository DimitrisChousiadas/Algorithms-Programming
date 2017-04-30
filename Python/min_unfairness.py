'''
    Given N positive integers, N > 1, and an integer 1 < K <= N, we want to find
    what is the minimum unfairness in a set of K numbers selected from the N initial ones.

    The minimum unfairness is defined as the difference between the max value and the min value in the set.

    To do that, we first sort the input integers and put them in an list numbers.

    Then, starting from the first integer, until the (N-K)th integer, we calculate the difference numbers[i+K-1] - numbers[i].
    The minimum unfairness is the minimum of these values.

    The rational behind this is the following:
        We are looking for sets with K numbers in them, and, so, inevitably, the minimum value of all the possible sets
        will be one of the first N-K+1 elements of the list, since the list is sorted.
        Now, given the minimum value of a set, in order to minimize the unfairness in that set, we need the minimum maximum value that
        we can include in the set.
        If the min value is at position i in the list, the min max value will be at position i+K-1 (since the set has to have K elements)

    This is, then, a greedy algorithm that runs in O(nlogn), since we have to sort the input.
    We can then find the min unfairness by traversing the array in O(N-K) time.
'''

def find_min_unfairness (numbers, k):
    l = len(numbers)
    val = numbers[l-1] - numbers[0]
    for i in range(l-k+1):
        test = numbers[i+k-1] - numbers[i]
        if (test < val):
            val = test
    return val

def main ():
    print("Enter the parameter N:")
    n = int(input())
    print("Enter the parameter K")
    k = int(input())
    if (n < 2 or k < 2 or k > n):
        print ("N must be greater than 1, K must be greater than 1 and N must be greater than or equal to K")
    else:
        numbers = []
        for i in range(n):
            numbers.append(int(input()))
        numbers.sort()
        val = find_min_unfairness(numbers, k)
        print("The minimum value of unfairness is: ", val)

main()
