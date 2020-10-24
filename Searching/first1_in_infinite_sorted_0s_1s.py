# Python 3 implementation to find the
# index of first 1 in an infinite
# sorted array of 0's and 1's

# function to find the index of first
# '1' binary search technique is applied
def indexOfFirstOne(arr, low, high):

    while (low <= high):
        mid = (low + high) // 2

        # if true, then 'mid' is the index
        # of first '1'
        if (arr[mid] == 1 and (mid == 0 or
                               arr[mid - 1] == 0)):
            break

        # first '1' lies to the left of 'mid'
        elif (arr[mid] == 1):
            high = mid - 1

        # first '1' lies to the right of 'mid'
        else:
            low = mid + 1

    # required index
    return mid

# function to find the index of first
# 1 in an infinite sorted array of 0's
# and 1's


def posOfFirstOne(arr):

    # find the upper and lower bounds between
    # which the first '1' would be present
    l = 0
    h = 1

    # as the array is being considered infinite
    # therefore 'h' index will always exist in
    # the array
    while (arr[h] == 0):

        # lower bound
        l = h

        # upper bound
        h = 2 * h

    # required index of first '1'
    return indexOfFirstOne(arr, l, h)


# Driver program
arr = [0, 0, 1, 1, 1, 1]
print("Index = ", posOfFirstOne(arr))
