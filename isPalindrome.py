def isPalindrome(string):
  if len(string)==1:
    return True
  if string[0]!=string[len(string)-1]:
    return False
  else:
    return isPalindrome(string[1:-1])
print(isPalindrome("malayalam"))
#output: True
