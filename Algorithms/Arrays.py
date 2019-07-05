def find_a_pair_with_given_sum(arr, res):
    # create a hash table
    hash_table = {}
    for i in range(len(arr)):
        if hash_table.get(res - arr[i]):
            print ("Pair found ", arr[i], res - arr[i])
        else:
            hash_table[arr[i]] = True

def check_subarray_with_zero_sum(arr):
    # create a set
    sumset = set()
    sumset.add(0)
    summation = 0
    for i in range(len(arr)):
        summation += arr[i]
        if (sumset.__contains__(summation)):
            return "The subarray exists"
        else:
            sumset.add(summation)
    return "The subarray does not exist"

def sort_binary_array(arr):
    # count the no of 1s and no of 2s
    print ("Original Array: ", arr)
    count = [0, 0]
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1
    for i in range(count[0]):
        arr[i] = 0
    for j in xrange(i+1, count[1]+count[0]):
        arr[j] = 1
    print ("Sorted Array: ",arr)

def find_duplicate_in_limited_range(arr):
    # the array can only contain 1 to n-1 elements and only one element repeating
    # for each element arr[i], we invert the sign of an element present at index (arr[i] - 1)
    # if it is positive, if element is already negative then its already duplicate
    for i in range(len(arr)):
        if (arr[arr[i] - 1] > 0):
            arr[arr[i] - 1] = -1 * arr[arr[i] - 1]
        else:
            print("duplicate element is ", arr[i])

def find_largest_subarray_formed_by_integers(arr):
    
    
if __name__ == "__main__":
    '''
    arr = [2, 3, 5, 6, 7, 1, 10]
    find_a_pair_with_given_sum(arr, 17)
    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    print(check_subarray_with_zero_sum(arr))
    arr = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    sort_binary_array(arr)
    arr = [1, 2, 3, 4, 4]
    find_duplicate_in_limited_range(arr)
    '''
    arr = [2, 0, 2, 1, 4, 3, 1, 0]
    find_largest_subarray_formed_by_integers(arr)
    

    
