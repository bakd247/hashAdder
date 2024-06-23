def binarySearch(array, integer):
    low = 0
    high = (len(array))//2
    mid = 0
    
    while low <= high:

        mid = low + (high - low) //2
        if array[mid][0] < integer:
            low = mid + 1
        elif array[mid][0] > integer:
            high = mid - 1
        else:
            return array[mid][0], array[mid][1]
    return -1