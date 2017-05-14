# Smallest Common Element of two integer arrays
# Given two arrays of integers as input, we want to find the smallest common element between the arrays
# To do that, we first traverse the first array and we put its elements in a set.
# Then, we traverse the second array until we find a common element, which then becomes the smallest common element.
# Then, we continue traversing the second array and every time we find a smaller common element, we update the smallest common element.
# We return a (True, elem) pair, with the smallest common element, if it exists.
# If it doesn't exist, we return (False, 0).
# This is an 0(n) algorithm (where n is the length of the larger array), since we traverse the arrays once and all operations on the set, on average, require 0(1) time.

def find_sce (arr1, arr2):

    s = set()
    for i in arr1:
        s.add(i)

    i = 0
    flag = False
    while i < len(arr2) and not flag:
        if arr2[i] in s:
            sce = arr2[i]
            flag = True
        i += 1
    while i < len(arr2):
        if arr2[i] < sce and arr2[i] in s:
            sce = arr2[i]
        i += 1

    if flag:
        return (True, sce)
    else:
        return (False, 0)

def main ():
    print("Enter the first input array:")
    arr1 = [int(x) for x in input().split()]
    print("Enter the second input array:")
    arr2 = [int(x) for x in input().split()]
    (flag, elem) = find_sce(arr1, arr2)
    if flag:
        print("The smallest common element is", elem)
    else:
        print("There is no common element between the arrays")

main()
