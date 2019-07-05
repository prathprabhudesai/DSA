''' there are different methods for the search in this module'''
import math

def LINEAR_SEARCH(arr, key):
    no_of_elements = len(arr)
    for i in range(no_of_elements):
        if (arr[i] == key):
            print("\n" + str(key) + " is present at index " + str(i))
            return i
    print("\n" + str(key) + " is not present in the array")
    return None

def BS_util(arr, start, last, key):
    if (last >= start):
        mid = int((start + last)/2)
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return BS_util(arr, start, mid - 1, key)
        else:
            return BS_util(arr, mid + 1, last, key)
    else:
        return None

def BINARY_SEARCH(arr, key):
    start = 0
    last = len(arr) - 1
    found_index = BS_util(arr, start, last, key)
    if (found_index is not None):
        print("\n"+ str(key) + " is present at index " + str(found_index))
        return found_index
    else:
        print("\n"+ str(key) + " is not present in the array")
        return None

#TODO: Fix the errors
def JUMP_SEARCH(arr, key):
    # just like binary search which partitions array in two equal size parts every time
    # jump search finds a particular partition by jumping m steps each time
    # and once we found the partition do the linear seach in that partition
    # this also requires array to be sorted
    # n the worst case, we have to do n/m jumps and
    # if the last checked value is greater than the element to be searched for,
    # we perform m-1 comparisons more for linear search.
    # Therefore the total number of comparisons in the worst case will be ((n/m) + m-1).
    # The value of the function ((n/m) + m-1) will be minimum when m = root(n).
    # Therefore, the best step size is m = root(n).
    # O(root(n)) time
    n = len(arr)
    step = step1 = int(math.sqrt(n))

    # find the block to find an element
    index  = 0
    while ((arr[index] <= key) and (index < n)):
        if (arr[index] == key):
            print("\n " + str(key) + " is present at index %d"%(index))
            return index
        index += step
        if (index >= n):
            index = n - 1
    if ((index <= (n - step)) and (index > 0)):
        window_start = index - step
        window_end = index
    else:
        window_start = index
        window_end = n
    # now perform linear search
    for i in xrange(window_start, window_end):
        if (arr[i] == key):
            print("\n " + str(key) + " is present at index %d"%(i))
            return i
    print("\n " + str(key) + " is not present in the array")
    return -1


def INTERPOLATION_SEARCH(arr, key):
    # Given a sorted array of n uniformly distributed values arr[],
    # write a function to search for a particular element x in the array.
    # interpolation search is an improvement over binary search
    # where values in a sorted array are uniformly distributed
    # interpolation search may go to different locations according
    # to the value of the key being searched
    #  if the value of the key is closer to the last element,
    # interpolation search is likely to start search toward the end side
    # O(log log n)
    lo = 0
    hi = len(arr) - 1
    while((lo <= hi) and (key >= arr[lo]) and (key <= arr[hi])):
        if (lo == hi):
            if (arr[lo] == key):
                return lo
            return -1
        # Probing the position with keeping 
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo)/(arr[hi] - arr[lo]))*(key - arr[lo])))
        # check if the key as at pos
        if arr[pos] == key: 
            return pos
        # if key is larger
        if arr[pos] < key:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1 
    
def EXPONENTIAL_SEARCH(arr, key):
    # 1. Find range where element is present
    # 2. Do Binary Search in above found range.
    # The idea is to start with subarray size 1,
    # compare its last element with key,
    # then try size 2, then 4 and so on until
    # last element of a subarray is not greater.
    # Once we find an index i (after repeated doubling of i),
    # we know that the element must be present between i/2 and i
    # (Why i/2? because we could not find a greater value in previous iteration)
    # O(log n)
    n = len(arr)
    if arr[0] == key:
        return 0

    i = 1
    while ((i < n) and (arr[i] <= key)):
        i = i * 2
    return BS_util(arr, i/2, min(i,n), key)

def FIBONACCI_SEARCH(arr, key):
    # Fibonacci Search divides given array in unequal parts
    # Binary Search uses division operator to divide range.
    # Fibonacci Search doesn't use division, but uses plus and minus.
    # The division operator may be costly on some CPUs.
    # Fibonacci Search examines relatively closer elements in subsequent steps.
    # So when input array is big that cannot fit in CPU cache or even in RAM,
    # Fibonacci Search can be useful.
    # The idea is to first find the smallest Fibonacci number
    # that is greater than or equal to the length of given array.
    # Let the found Fibonacci number be fib (m'th Fibonacci number).
    #  We use (m-2)'th Fibonacci number as the index (If it is a valid index)
    # Let (m-2)'th Fibonacci Number be i, we compare arr[i] with x, if x is same, we return i
    #  Else if x is greater, we recur for subarray after i, else we recur for subarray before i.
    n = len(arr)
    fib2 = 0 # m-2 fib no
    fib1 = 1 # m-1 fib no
    fibm = fib2 + fib1
    while(fibm < n):
        fib2 = fib1
        fib1 = fibm
        fibm = fib2 + fib1
    offset = -1
    while (fibm > 1):
        i = min(offset + fib2, n-1)
        if (arr[i] < key):
            fibm = fib1
            fib1 = fib2
            fib2 = fibm - fib1
            offset = i
        elif (arr[i] > key):
            fibm = fib2
            fib1 = fib1 - fib2
            fib2 = fibm - fib1
        else:
            return i
    if (fib1 and arr[offset + 1] == key):
        return offset + 1
    return -1

def OPTIMAL_BINARY_SEARCH(arr, key):
    #  Given a sorted array of N distinct elements.
    # Find a key in the array using least number of comparisons.
    # theoretically we need log(n) + 1 comparisons at worst
    # if we observe we are using two comparisons actually each iteration
    # except the last iteration where the search is successful
    start = 0
    last = len(arr) - 1
    while ((last - start) > 1):
        mid = start + int((last - start)/2);
        if (arr[mid] <= key):
            start = mid
        else:
            last = mid
    if (arr[start] == key):
        return start
    elif (arr[last] == key):
        return last
    else:
        return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #LINEAR_SEARCH(arr, 4)    
    #BINARY_SEARCH(arr, 3)
    #JUMP_SEARCH(arr, 10)
    #INTERPOLATION_SEARCH(arr, 9)
    #EXPONENTIAL_SEARCH(arr, 1)
    #FIBONACCI_SEARCH(arr, 8)
    #OPTIMAL_BINARY_SEARCH(arr, 10)
