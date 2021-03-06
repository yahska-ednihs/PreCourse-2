# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n) = n log n
# Space Complexity : O(n) = n
# Did this code successfully run on Leetcode : I did not try.  Will do soon
# Any problem you faced while coding this : Yes, I had forgotten the partition part of the algorithm. I had to revise it.


# Your code here along with comments explaining your approach
# give you explanation for the approach
def partition(arr,low,high): #O(n) = n
    i = low
    for j in range(low, high):
        if arr[high] >= arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
    temp = arr[high]
    arr[high] = arr[i]
    arr[i] = temp
    return i
  
    #write your code here

# Function to do Quick sort 
def quickSort(arr,low,high): #O(n) = log(n)
    if low<high:
        mid = partition(arr, low, high)
        quickSort(arr, low, mid-1)
        quickSort(arr, mid+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 6, 5] 
n = len(arr) 
quickSort(arr,0,n-1) #O(n) = nlog(n)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
