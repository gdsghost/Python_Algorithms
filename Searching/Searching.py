def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


def interpolationSearch(arr, n, x):
    # Find indexs of two corners
    lo = 0
    hi = (n - 1)

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) /
                         (arr[hi] - arr[lo])) * (x - arr[lo])))

        # Condition of target found
        if arr[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            lo = pos + 1

        # If x is smaller, x is in lower part
        else:
            hi = pos - 1

    return -1


array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

result = linearSearch(array, len(array), x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

result = interpolationSearch(array, len(array), x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

# FIRST REPEATED ELEMENT
A = [3, 2, 1, 2, 2, 3]
d = {i: 0 for i in A}
print(d)

for i in A:
    d[i] = d[i]+1

print(d)

for key, value in d.items():
    if value > 1:
        print("KEY", key)
        break

# PAIR OF ELEMENTS WHOSE SUM IS GIVEN TO A NUMBER


def printPairs(arr, arr_size, sum):
    for i in arr:
        temp = sum-i
        if temp in arr:
            print("THE PAIR IS {} and {}".format(i, temp))


A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)


# TWO ELEMENTS WHOSE SUM CLOSEST TO 0
def minAbsSumPair(arr, n):

    # Variables to keep track
    # of current sum and minimum sum
    sum, min_sum = 0, float('inf')

    # left and right index variables
    l = 0
    r = n - 1

    # variable to keep track of
    # the left and right pair for min_sum
    min_l = l
    min_r = n - 1

    # Array should have at least two elements*/
    if(n < 2):
        print("Invalid Input", end="")
        return

    # Sort the elements */
    arr.sort()

    while(l < r):
        sum = arr[l] + arr[r]

        # If abs(sum) is less
        # then update the result items
        if(abs(sum) < abs(min_sum)):
            min_sum = sum
            min_l = l
            min_r = r
        if(sum < 0):
            l += 1
        else:
            r -= 1

    print("The two elements whose sum is minimum are",
          arr[min_l], "and", arr[min_r])
    # Time Complexity: complexity to sort + complexity of finding the optimum pair = O(nlogn) + O(n) = O(nlogn)


# Driver Code
arr = [1, 60, -10, 70, -80, 85]
n = len(arr)
minAbsSumPair(arr, n)


# SEPARATE EVEN AND ODD NUMBER
A = [12, 34, 45, 9, 8, 90, 3]
c = -1
for i in range(len(A)):
    if A[i] % 2 == 0:
        c += 1
        A[c], A[i] = A[i], A[c]

print(A)


A = [1, 2, 3, 4, 5, 6]
sum = 6
for i in A:
    for j in A:
        if (sum-(i+j)) in A:
            print("{} {} {}".format(i, j, sum-(i+j)))
