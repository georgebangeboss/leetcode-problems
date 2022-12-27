# uses start and end pointers and while loop
def isPalindrome0(s):
    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


# using for loop (this is more optimal approach than ispalindrome0)
def isPalindrome1(s):
    last = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[last - i]:
            return False

    return True


# Reverse the string using extended slice and then compare
def isPalindrome2(s):
    return s == s[::-1]


# reverse the string using inbuilt reversed function and then compare
def isPalindrome3(s):
    rev = "".join(reversed(s))
    return s == rev


# reverse using for loop and then compare
def isPalindrome4(s):
    rev = ""
    for c in s:
        rev = c + rev
    return s == rev


# uses start and end pointers(negative notation) and while loop, just a decorated isPalindrome0
def isPalindrome5(s):
    start = 0
    end = -1

    while start <= len(s) + end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


# using recursion
def isPalindrome6(s):
    length = len(s)
    if length <= 1:
        return True
    last = length - 1
    if s[0] != s[last]:
        return False
    else:
        return isPalindrome6(s[1 : length - 1])


print(isPalindrome6("racecar"))
