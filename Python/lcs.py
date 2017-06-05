'''
Longest common substring between two strings
'''

def max3 (a, b, c):
    if a >= b and a >= c:
        return a
    if b >=a and b >= c:
        return b
    else:
        return c

# A recursive implementation of finding the longest common substring
# of characters between two string
# Let s1 and s2 be two char arrays, representing the two strings of the input.
# if we consider the first i and j characters, from s1 and s2 respectively, then
# the longest common substring of the substrings s1[:i] and s2[:j] is:
#   LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1)), if these two characters are different
#   LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1), 1+LCS(i-1, j-1)), if the characters are equal
# Using this recursion, we can implement the following recursive function
def lcs_recursive (s1, s2):
    if not s1:
        return 0
    elif not s2:
        return 0
    else:
        l1 = len(s1)
        l2 = len(s2)
        c1 = s1[l1-1]
        c2 = s2[l2-1]
        case1 = lcs(s1[:l1-1], s2)
        case2 = lcs(s1, s2[:l2-1])
        if (c1 == c2):
            case3 = lcs(s1[:l1-1], s2[:l2-1])
        else:
            case3 = -1
        return max3(case1, case2, case3 + 1)


# Longest common substring, using dynamic programming
# Using the same recursion as before, we can solve the problem, only this time with dynamic programming.
# We are going to use an array with len(s1)+1 rows and len(s2)+1 columns.
# The cell (i,j) of the array will the length of the longest common substring
# of the two strings, up until the positions i and j respectively.
# At the end, what we want is the value of the cell (len(s1), len(s2)).
def lcs_dynamic (s1, s2):

    lcs = []
    lcs.append([])
    for i in range(len(s2)+1):
        lcs[0].append(0)

    for c1 in range(1, len(s1)+1):
        for c2 in range(len(s2)+1):
            if c2 == 0:
                lcs.append([0])
            else:
                case1 = lcs[c1-1][c2]
                case2 = lcs[c1][c2-1]
                char1 = s1[c1-1]
                char2 = s2[c2-1]
                if (char1 == char2):
                    case3 = lcs[c1-1][c2-1]
                else:
                    case3 = -1
                lcs[c1].append(max(case1, case2, case3 + 1))

    return lcs[len(s1)][len(s2)]


print("Enter the first string:")
str1 = list(input())
print("Enter the second string:")
str2 = list(input())
print("The lenght of the longest common substring is:")
print(lcs_dynamic(str1, str2))
