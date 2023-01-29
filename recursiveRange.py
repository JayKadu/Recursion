def recursiveRange(num):
  if num==0:
    return 0
  else:
    return nums + recursiveRange(num-1)
print(recursiveRange(6))
#output: 21
