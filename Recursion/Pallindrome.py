
def pallindrome(str, i, j):
    if i >= j: return True
    if str[i] != str[j]: return False
    return pallindrome(str, i+1, j-1)

## Driver Code
string = "racecar"
i = 0
j = len(string) - 1
print(pallindrome(string, i, j))