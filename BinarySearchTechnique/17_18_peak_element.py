# Find PEAK element and find maximum element in bitonic array; both have exactly same code
# Peak element array:
#       This array could have more than one peak element
#       2, 4, 7, 6, 12, 11, 9, 3 -> 12 & 7
#       2, 4, 7, 12, 14          -> Last element; 14
#       12, 10, 7, 2, 4          -> First element; 12
#       12, 12, 13, 14, 15, 15
# Bitonic element:
#       Array with monotonously increase followed by monotonously decreasing fashion.
#       No duplicates found in this array; Only one peak will be present in such arrays
#       1, 3, 4, 5, 6, 7, 5, 4, 2, 1
import logging
logging.basicConfig(level=logging.INFO)


def peak_element_in_given_array(arr):
    """
    Find the peak element in the given array.

    1. Peak element is the one which is greater than both of its neighbour.
    2. There can be more than one peak element in an array
    3. For edge elements,
        First element is peak of its greater than next element
        Last element is peak if its greater than previous element
    4. Peak element is always found at higher neighbour element side because
        For element to be peak, it should be greater than both of its neighbour
    5. greater neighbour have the advantage as its already greater than one
        of its neighbout(current mid)

    Logic:
        For non-edge elements
            if element is greater than right and left elements,
                return a[mid]
            else
                Move towards element greater than current element
        for edge elements:
            for first element, check if its greater than 2nd element
                if yes, return it as peak
            for last element, check if its greatern than last but one element
                if yes, return it as peak
        return "No peak"
    """
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = low + (high-low)//2
        # check for non edge elements
        if mid > 0 and mid < len(arr)-1:
            # check if element is greater than both of its neighbour
            logging.debug('Not an edge condition')
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                # this element is greater than both of its neighbout
                logging.debug('%s is greater than both of its neighbour'
                              '(%s and %s)', arr[mid], arr[mid-1], arr[mid+1])
                return arr[mid]
            elif arr[mid-1] > arr[mid]:
                # Peak element if always found towards greater element side
                logging.debug('%s: Left element(%s) is greater, going left', arr[mid], arr[mid-1])
                high = mid-1
            else:
                logging.debug('%s: right element(%s) is greater, going right', arr[mid], arr[mid+1])
                low = mid+1
        else:
            # this is hit for edge conditions
            logging.debug('Edge element')
            # first element is peak if its greater than its right neighbour
            if mid == 0 and arr[mid] > arr[mid+1]:
                logging.debug('First element is the peak element')
                return arr[mid]
            # Last element is peak if its greater than its left neighbour
            elif mid == len(arr)-1 and arr[mid] > arr[mid-1]:
                logging.debug('Last element is peak element')
                return arr[mid]
            else:
                # this is hit when no peak element is found;
                # Probably last two or first two elements are equal
                logging.debug('No peak elements found in this array')
                return -1

# One peak element array
arr1 = [2, 4, 7, 9, 12, 11, 9, 3]
result = peak_element_in_given_array(arr1)
print(result)

# two peak elements array
arr2 = [2, 4, 7, 6, 12, 11, 9, 3]
result = peak_element_in_given_array(arr2)
print(result)

# last element as peak
arr3 = [2, 4, 7, 12, 14]
result = peak_element_in_given_array(arr3)
print(result)

# first and last element as peak
arr3 = [12, 10, 7, 2, 4]
result = peak_element_in_given_array(arr3)
print(result)

# first and last element as peak
arr3 = [12, 10, 7, 2, 0]
result = peak_element_in_given_array(arr3)
print(result)

# No peak elements array
arr3 = [12, 12, 13, 14, 15, 15]
result = peak_element_in_given_array(arr3)
print(result)
