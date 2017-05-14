# Anagrams
# Given a list of words, we want to find which ones are mutual anagrams with the others.
# For example, the words man and nam are mutual anagrams, so are the words sun and nus.
# So, the corresponding output of the list (man, nam, sun, nus) are the groups (man, nam) and (sun, nus).
# To do that, we use a dictionary and we traverse the input list.
# For each word in the list, we convert all letters into lower case and we sort them. If the sorted word exists as key in the dictionary,
# then we append the word to the values that correspond to that key.
# If it doesn't exist, then we add it to the dictionary, with the word as its value.

def find_anagrams (words):
    s = {}
    for w in words:
        key = ''.join(sorted(w.lower()))
        if key in s:
            foo = s[key]
            foo.append(w)
            s[key] = foo
        else:
            s[key] = [w]

    return s

def main ():
    print("Enter the list of words:")
    words = [w for w in input().split()]
    anagrams = find_anagrams(words)
    print("The groups of mutual anagrams are:")
    for key in anagrams:
        print(anagrams[key])

main()
