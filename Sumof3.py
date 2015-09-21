array = [-3,-2,0,1,4,6]
for i in range(1,(len(array) - 1)):
  iter = i + 1
  reviter = len(array) - 1
  while (iter < reviter):
    tmp = array[iter] + array[reviter] + array[i]
    if(tmp > 0):
        reviter = reviter - 1
    elif (tmp < 0):
        iter = iter + 1
    else:
        print("yes")
        break
