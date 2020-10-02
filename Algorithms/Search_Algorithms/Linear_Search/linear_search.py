def search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1
    
arr=input().split() # inputs the numbers
x=input() # inputs the number to be searched

result=search(arr, x)
print(result)
