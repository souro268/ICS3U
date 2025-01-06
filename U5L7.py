def fib(n):
    if(n==1):
        arr.append(1)
        return arr
    if(n==2):
        arr.append(1)
        fib(1)
        return arr
    if n>2:
      fib(n-1)
      a=arr[len(arr)-1]+arr[len(arr)-2]
      arr.append(a)
      return arr
      
arr=[]
seq = fib(45)
print(seq)
