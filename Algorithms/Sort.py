''' there are different methods for sorting in this module '''

def SWAP(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def BUBBLE_SORT(arr):
    # Bubble Sort is the simplest sorting algorithm that works
    # by repeatedly swapping the adjacent elements if they are
    # in wrong order.
    # we can optimize it a little by adding a check if there is
    # a swap in the inner loop
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if (arr[j] > arr[j+1]):
                SWAP(arr, j, j+1)
                swapped = True
        if(not swapped):
            break
            
def SELECTION_SORT(arr):
    # sorts an array by repeatedly finding the minimum element
    # (considering ascending order) from unsorted part
    # and putting it at the beginning
    n = len(arr)
    for i in range(n):
        minidx = i
        for j in range(i+1, n):
            if arr[minidx] > arr[j]:
                minidx = j
        SWAP(arr, i, minidx)

def INSERTION_SORT(arr):
    # works the way we sort playing cards in our hands
    # put element a[i] in the sorted array from a[0...i-1]
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def MERGE_SORT_MERGE(a1, a2, out):
    i1 = i2 = iout = 0
    while((i1 < len(a1)) or (i2 < len(a2))):
        if ((i2 >= len(a2)) or ((i1 < len(a1)) and (a1[i1] < a2[i2]))):
            out[iout] = a1[i1]
            i1 += 1
        else:
            out[iout] = a2[i2]
            i2 +=1
        iout += 1

def MERGE_SORT(arr):
    # divides input array in two halves, calls itself for the
    # two halves and then merges the two sorted halves
    if (len(arr) > 1):
        mid = len(arr)//2 # floor division
        a1 = arr[:mid]
        a2 = arr[mid:]
        MERGE_SORT(a1)
        MERGE_SORT(a2)
        MERGE_SORT_MERGE(a1, a2, arr)

def QUICK_SORT_PARTITION(arr, left, right, pivot):
    while(left <= right):
        while(arr[left] < pivot):
            left += 1
        while(arr[right] > pivot):
            right -= 1
        if (left <= right):
            SWAP(arr, left, right)
            left += 1
            right -= 1
    return left
        
def QUICK_SORT_UTIL(arr, left, right):
    if (left >= right):
        return
    pivot = arr[(left + right)//2]
    index = QUICK_SORT_PARTITION(arr, left, right, pivot)
    QUICK_SORT_UTIL(arr, left, index-1)
    QUICK_SORT_UTIL(arr, index, right)

def QUICK_SORT(arr):
    QUICK_SORT_UTIL(arr, 0, len(arr)-1)

def COUNT_SORT(arr):
    # a sorting technique based on keys between a specific range.
    # It works by counting the number of objects having distinct key values
    # (kind of hashing). Then doing some arithmetic to calculate
    # the position of each object in the output sequence.
    # mostly it will be used to sort the strings as we know the specific range
    # O(n+k) the range of elements is 1 to K
    min_no = min(arr)
    max_no = max(arr)
    count = [0]*(max_no - min_no + 1)
    index = 0
    for i in range(len(arr)):
        count[arr[i] - min_no] += 1
    for i in range(len(count)):
        if count[i] != 0:
            for j in range(count[i]):
                arr[index] = i + min_no
                index += 1

def MODIFIED_COUNTING_SORT(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(0, n):
        index = (arr[i]/exp)
        count[(index)%10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = arr[i]/exp
        output[count[index%10] - 1] = arr[i]
        count[index%10] -= 1
        i -= 1
    arr[:] = output[:]
    

def RADIX_SORT(arr):
    # What if the elements are in range from 1 to sqr(n)
    # We can't use counting sort because counting sort will take O(n2)
    # which is worse than comparison based sorting algorithms.
    # The idea of Radix Sort is to do digit by digit sort starting from
    # least significant digit to most significant digit.
    # Radix sort uses counting sort as a subroutine to sort.
    '''Let there be d digits in input integers. 
    Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, 
    for example, for decimal system, b is 10. What is the value of d? If k is the maximum possible value, 
    then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)). 
    Which looks more than the time complexity of comparison based sorting algorithms for a large k. 
    Let us first limit k. Let k <= nc where c is a constant. 
    In that case, the complexity becomes O(nLogb(n)). 
    But it still doesn't beat comparison based sorting algorithms. 
    What if we make value of b larger?. 
    What should be the value of b to make the time complexity linear? 
    If we set b as n, we get the time complexity as O(n). 
    In other words, we can sort an array of integers with range from 1 to nc 
    if the numbers are represented in base n (or every digit takes log2(n) bits).
    Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort? 
    If we have log2n bits for every digit, the running time of Radix appears to be 
    better than Quick Sort for a wide range of input numbers. 
    The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort 
    uses hardware caches more effectively. Also, Radix sort uses counting sort as a subroutine 
    and counting sort takes extra space to sort numbers.'''
    # find the maximum no to know the max no of digits
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        MODIFIED_COUNTING_SORT(arr, exp)
        exp *= 10

def BUCKET_SORT(fl_arr):
    # when you have floating point nos
    # you can't use the counting sort since indexes can't be float values
    # then what to do? bucket sort is the answer
    # create buckets like histogram
    # insertion sort on each bucket
    # so used basically for the 
    arr = []
    slots = 10
    for i in range(slots):
        arr.append([])
    for i in fl_arr:
        index = int(slots*i)
        arr[index].append(i)
    for i in range(slots):
        INSERTION_SORT(arr[i])
    # merge all the buckets
    k = 0
    for i in range(slots):
        for j in range(len(arr[i])):
            fl_arr[k] = arr[i][j]
            k += 1

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 64, 64, 64, 34, 34, 34, 12, 12]
    #fl_arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Input array: ", arr)
    # BUBBLE_SORT(arr)
    # SELECTION_SORT(arr)
    # INSERTION_SORT(arr)
    # MERGE_SORT(arr)
    # QUICK_SORT(arr)
    # COUNT_SORT(arr)
    # RADIX_SORT(arr)
    # BUCKET_SORT(fl_arr)
    print("Sorted array: ", arr)
