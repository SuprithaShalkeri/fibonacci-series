def FiboRecursion(n):
  if n<=1:
    return n
  else:
    return(FiboRecursion(n-1)+ fiborecursion(n-2))

nterms=int(input("enter the terms?"))
if nterms <= 0:
  print("please enter a positive interger")

else:
    print("fibonacci sequence:")
    for i in range(nterms):
      print(fiborecursion(i)) 0
