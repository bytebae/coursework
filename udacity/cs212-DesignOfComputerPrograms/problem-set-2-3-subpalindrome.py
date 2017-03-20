# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.lower()
    best_length = (0, 0)
    odd_lengths = [ palindromes_centered_at_i(i, i, text) for i in range(len(text)) ]
    even_lengths = [ palindromes_centered_at_i(i, i+1, text) for i in range(len(text) - 1) ]
    return max([best_length] + odd_lengths + even_lengths, key=lambda (x, y): y - x + 1)

def palindromes_centered_at_i(lp, rp, text):
    # centered at i, find all palindromes, till boundary conditions are met
    best_length = (lp, rp+1) if lp == rp else (0, 0)
    while lp >= 0 and rp < len(text):
        if text[lp] != text[rp]:
            break
        best_length = (lp, rp + 1)
        lp -= 1
        rp += 1

    return best_length

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()





# def is_palindrome(t):
#     s = str(t).lower()
#     return s == s[::-1]

# def slower_longest_subpalindrome_slice(text):
#     "Return (i, j) such that text[i:j] is the longest palindrome in text."
#     # Your code here
#     # first start with the brute force solution
#     l = len(text)
#     if l == 0:
#         return (0, 0)
#     palindrome_pool = [(text[i:j], (i, j))
#                        for i in range(l+1)
#                        for j in range(i+1, l+1)
#                        if is_palindrome(text[i:j])]
#     ret = list(max(palindrome_pool , key=lambda x: len(x[0])))
#     return ret[1]

