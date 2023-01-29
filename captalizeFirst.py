def captalizeFirst(arr):
  result=[]
  if len(arr)==0:
    return result
  else:
    result.append(arr[0][0].upper()+arr[0][1:])
  return result+ captalizeFirst(arr[1:])

print(captalizeFirst(['car', 'taco', 'banana']))

#output: ["Car", "Taco", "Banana"]
