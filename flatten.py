def flatten(arr):
  result=[]
  for i in arr:
    if type(i) is list:
      result.extend(flatten(i))
    else:
      result.append(i)
  return result

print(flatten([1, 2, 3, [4, 5]]))

#output: [1,2,3,4,5]
