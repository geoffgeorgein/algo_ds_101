def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
 
    for j in range(low, high):
 
        # If current element is smaller than or equal to pivot 
         
        if arr[j] <= pivot:
 
            # increments the index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 

# arr[] Array to be sorted,
# low  Starting index,
# high   Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
       
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 

arr=input().split()
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print(arr[i])
