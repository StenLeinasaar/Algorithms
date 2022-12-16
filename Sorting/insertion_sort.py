import time
'''

Insertion sort is an efficent sorting algorithm for small values of n, where n is the number of elements to be sorted. 
It sorts elements in place. A lot like people sorting their hand when playing cards.

Pseduocode is as follows: 

INSERTION-SORT(A)
1. for j = 2 to A.length
2.      key = A[j]
3.      //insert A[j] into the sorted sequence A[1... j-1].
4.      i= j -1
5.      while i > 0 and A[i] > key
6.          A[i + 1] = A[i]
            i = i-1
        A[i+1] = key

'''


def insertion_sort(list):
    toSort = list
    print("Beginning to sort", toSort)
    for x in range(1, len(toSort)):
        key = toSort[x]
        #insert A[j] into the sorted sequence 
        i = x - 1
        while i >= 0 and toSort[i] > key:
            toSort[i + 1] = toSort[i]
            i = i - 1
        toSort[i + 1] = key
    print(toSort)
    return toSort


print(time.time())
insertion_sort([13,15,9,8,7,6,5,4,3,2,1])
print(time.time())