"""
    Given a string, we want to count how many pairs of substrings there are, so that
    the two substrings are anagrams of each other, i.e. they have the same set of characters.
    E.g. the string abba has 4 anagramatic pairs: (a, a), (ab, ba), (abb, bba) and (b, b).

    To do that, we keep a dictionary that maps character sets to the number of substrings that are formed by that set,
    and a counter that counts the number of anagramatic pairs.
    Then, for each of the n*(n+1)/2 substrings, we count the frequency of each character in the substring.
    Using the dictionary, if we have seen another substring with the same key, that is the same frequency pattern,
    we increase the pairs counter by the current value of the dictionary in that key, and then, we increase the value by one.
    If, on the other hand, the key doesn't exist in the dictionary, we put it in it, with a value equal to one.

    The above implementation takes O(n^3) time, since we consider all possible substrings and for each substring we count the
    number of appearances of its characters using a collections.Counter in O(n) time and then create a frozenset with the result,
    with which we access the dictionary in O(1) time and update it, again, in O(1) time.

    The input that the program expects is, first an integer t that denotes the number of testcases,
    and then, t lines with the t input strings.
    The output is t lines, where each line has the number of anagramatic pairs in the respective input string.

    Sample input:
    2
    abba
    abcd
    Sample output:
    4
    0
"""

from collections import Counter

def anagramatic_pairs (string):
    anagrams = {}
    pairs = 0
    l = len(string)
    for i in range(l):
        for j in range(i+1, l+1):
            substr = string[i:j]
            # Instead of Counter, we could do the following to count the number
            # of appearances of the characters in a substring.
            # These two ways are, virtually, the same, since Counter is a subclass of dict.
            """
            chars = {}
            for c in substr:
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 1
            key = frozenset(chars.items())
            """
            key = frozenset(Counter(substr).items())
            if key in anagrams:
                count = anagrams[key]
                pairs += count
                anagrams[key] = count + 1
            else:
                anagrams[key] = 1

    return pairs


if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        string = input().strip().lower()
        print(anagramatic_pairs(string))
