import math
'''
MERGE(A, p, q, r)
1. n1 = q - p + 1
2. n2 = r - q
3. let L[1.. n1 + 1] and R[1.. n2 + 1] be new arrays
4. for i = 1 to n1
5.      L[i] = A[p + i - 1]
6. for j = 1 to n2
7.      R[j] = A[q + j]
8. L[n1 + 1] = infinity
9. R[ n2 + 1] = infinity
10. i = 1
11. j = 1
12. for k = p to r
13.     if L[i] <= R[j]
14.         A[k] = L[i]
15.         i = i + 1
16.     else A[k] = R[j]
17.         j = j + 1


'''

def merge(arr, left_index, middle_index, right_index):
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index
 
    # create temp arrays
    left = [0] * (n1)
    right = [0] * (n2)
 
    # Copy data to temp arrays left[] and right[]
    for i in range(0, n1):
        left[i] = arr[left_index + i]
 
    for j in range(0, n2):
        right[j] = arr[middle_index + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left_index     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
    


'''
MERGE-SORT(A, p, r)
1. if p < r
2.      q = floor((p+r) /2 )
3.      MERGE-SORT(A, p , q)
4.      MERGE-SORT(A, q + 1, r)
5.      MERGE(A, p, q, r)
'''

def mergeSort(arr, left_index, right_index):
    if left_index < right_index:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        middle_index = left_index+(right_index-left_index)//2
        # Sort first and second halves
        mergeSort(arr, left_index, middle_index)
        mergeSort(arr, middle_index+1, right_index)
        merge(arr, left_index, middle_index, right_index)

# Driver code to test above
arr = [15,13,12, 11, 13, 5, 6,22, 7]
n = len(arr)
print("Given array is", arr)
mergeSort(arr, 0, n-1)
print("\n\nSorted array is", arr)

