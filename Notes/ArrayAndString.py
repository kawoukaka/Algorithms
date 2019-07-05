# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# input: 'asdfnzxmncv'
def isUnique(s):
    temp = ''
    for char in sorted(s):
        if char != temp:
            temp = char            
        else:
            return False
    return True
print(isUnique('asdfnzxmcv'))
print(isUnique('asdfnzxmccv'))

# Given two strings, write a method to decide if one is a permutation of the other.
# input: ['abc', 'bac']
def isPermutation(arr):
    temp = ''
    for string in arr:
        if temp == sorted(string):
            return True
        else:
            temp = sorted(string)
    return False

print(isPermutation(['abc', 'bac']))
print(isPermutation(['abc', 'bacd']))

# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE"
# Input: "Mr John Smith"
# Output: "Mr%20John%20Smith"
def urlify(s):
    return '%20'.join(s.split(' '))
print(urlify('Mr John Smith'))
    
# Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
def palindromePermutation(s):
    if s == s[::-1]:
        return True
    return False


# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pales, pale -> true
# pale, bale -> true
# pale, bake -> true
# pale, bike -> false
def oneAway(s1, s2):
    temp = {}
    indx = 0
    for char in s1:
        temp[char] = temp
        indx += 1
    count = 0
    for char in s2:
        if count > 1:
            return False
        if char not in temp:
            count += 1
    return True
print(oneAway('pales', 'pale'))
print(oneAway('pales', 'bike'))

# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
def stringCompression(s):
    len_s = len(s)
    new_s = ''
    count = 0
    for i in range(len_s):
        count += 1
        if i + 1 >= len_s or s[i] != s[i+1]:
            new_s += s[i] + str(count)
            count = 0
    return new_s if len(new_s) < len_s else s
print(stringCompression('aabcccccaaa'))


# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotateMatrix():
    pass

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def zeroMatrix():
    pass

# Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
def stringRotation():
    pass