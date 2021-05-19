# entering lenth of list 

a = int(input("enter lenth of list"))

lis = []

# entering number of list

for i in range(a):

  lis_ele = int(input("enter number of list"))

  lis.append(lis_ele)

# function of palindrome 

def func(n):

  m = n

  while fun2(m):

    m+=1

  return(m)

def fun2(h):

  a = str(h)[::-1] == str(h)

  if a == True:

    b = False

  else:

    b = True

  return b

  

# print palindrome of entering list or number

for i in lis:

  z = func(i)

  print("Next palindrome of {} is {}").format(i,z)

''' plese like and comment'''
