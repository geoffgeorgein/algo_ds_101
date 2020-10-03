def sumofncube(n):
    s=0
    for i in range(1,n+1):
        s=s+(i*i*i)  #finds the sum
    return s
n=int(input()) #inputs the limit n
sum = sumofncube(n)
print(sum)
  
