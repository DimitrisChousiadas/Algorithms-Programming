# Google mock interview on YouTube
# Given a list of integers and a target integer
# we want to find all the unique pairs of numbers in the list that add up to the target number.
# To do that, we scan the input list and we use a "comp" set, that stores the complements of each number in the list and a "results" set to store the results.
# A complement of a number is defined as the difference target - number.
# Concretely, for each number in the list, we look for it in the "comp" set.
# If we find it, it means that we have seen its complement earlier in the list.
# In that case, we add the pair (number, complement) in the "results" set and we add the complement in the "comp" set.
# If we don't find it, we just add the complement in the "comp" set.
# In order to only keep the unique pairs, we order the two members of a pair before adding it in the "results".
# Since the lookup and insertion operations on a set take O(1) on average, the algorithm has a time complexity of O(n).

def scan_list (nums, target):

    comp = set()
    results = set()
    for n in nums:
        if n in comp:
            if n < target/2:
                results.add((n, target-n))
            else:
                results.add((target-n, n))
        comp.add(target - n)

    if not results:
        print("No pair of numbers adds up to the target sum!")
    else:
        print("The following pairs add up to the target sum:")
        for pair in results:
            print(pair)

if __name__ == "__main__":

    print("Enter the list of numbers:")
    nums = [int(x) for x in input().split()]
    while not nums:
        print("The list should be non empty! Enter the list:")
        nums = [int(x) for x in input().split()]

    print("Enter the target sum:")
    target = input()
    while not target:
        print("Enter the target sum:")
        target = input()
    target = int(target)

    scan_list(nums, target)
