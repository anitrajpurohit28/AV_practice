import logging

logging.basicConfig(level=logging.DEBUG)

class Solution:
    def no_of_rotation(self, arr):
        """
        Number of times a sorted array is rotated

        1. index of minimum element is equal to number of times array is rotated.
        start ....... mid ........ end;
        2. if start <= mid: left part of array is sorted
        3. if mid <= end: right part of array is sorted
        4. Minimum elemnt if always found in unsorted part of array

        Args:
            array in which number of rotation is to be found
        Returns:
            0:     if input array is sorted
            index: otherwise
        """
        low = 0
        high = len(arr) - 1
        arr_len = len(arr) -1

        # if first element is lesser than last element, array is already sorted
        if arr[low] <= arr[high]:
            logging.debug('input array is already sorted')
            return 0

        while low <= high:
            mid = low + (high-low)//2
            # mid+1 and mid-1 could lead to "IndexError: list index out of range"
            prev = (mid - 1 + arr_len ) % arr_len
            next = (mid + 1) % arr_len

            # find the index of minimum element;
            # the min element should be lesser than both its neighbour; Only one such occurance
            # will be present in sorted rotated array
            if arr[prev] >= arr[mid] <= arr[next]:
                logging.info('Found rotation at index %s', mid)
                return mid
            elif arr[0] <= arr[mid]:
                # if 0th index is lesser than mid index, left array is already sorted
                # smallest element will always be found in unsorted part of array
                low = mid + 1
            else: # arr[arr_len] < arr[mid]
                high = mid - 1

    def binary_search(self, arr, start_index, end_index, item):
        """
        Binaray search on array with given start and end index
        Args:
            Array: in which item is to be searched
            start_index: starting index
            end_index: end index
            item: Item to be searched for
        return:
            index: if the item to be searched for, is found
            -1: if the item is NOT found
        """
        logging.debug('BS on %s', arr[start_index:end_index])
        low = start_index
        high = end_index -1 # This is important observation, else will lead to Traceback
        while low <= high:
            mid = low + (high-low)//2
            logging.debug('Mid: %s; Low: %s; High: %s; arr[mid]: %s', mid, low, high, arr[mid])
            if item == arr[mid]:
                logging.debug('%s found at index %s', item, mid)
                return mid
            elif item < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        logging.debug('%s not found', item)
        return -1

    def find_item_in_sorted_rotated_arr(self, arr, item):
        """
        Find an item in sorted rotated array.
        Logic:
            1. Find the number of times array is rotated;
            2. Divide array at point where array is rotated;
            3. now, both the arrays will be sorted;
            4. Apply binary search on both the array's
        """
        logging.debug('Array: %s\nitem: %s', arr, item)
        # Find the number of rotation
        rotate_index = self.no_of_rotation(arr)
        logging.debug('No of rotation: %s', rotate_index)
        found_index = -1

        # apply BS on left array
        found_index = self.binary_search(arr, 0, rotate_index, item)
        if found_index == -1:
            # only if item is not found, apply BS on right array
            found_index = self.binary_search(arr, rotate_index, len(arr), item)

        # if the item is stil not found, return, NOT FOUND
        if found_index == -1:
            logging.info('Item NOT found in given array')
            return -1

        # We get here if the item is found; return the index
        logging.info('Item found at index %s', found_index)
        return found_index


ob = Solution()
print('===============')
arr1 = [6, 7, 8, 9, 1, 2]
result = ob.find_item_in_sorted_rotated_arr(arr1, 1)
print(result)

print('===============')
arr2 = [23, 34, 56, 77, 88, 20]
result = ob.find_item_in_sorted_rotated_arr(arr2, 20)
print(result)

print('===============')
arr3 = [23, 34, 56, 77, 88, 99]
result = ob.find_item_in_sorted_rotated_arr(arr3, 23)
print(result)

print('===============')
arr3 = [77, 88, 99, 23, 34, 56]
result = ob.find_item_in_sorted_rotated_arr(arr3, 58)
print(result)
print('===============')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().strip()]
        k = int(input())
        ob = Solution()
        print(ob.find_item_in_sorted_rotated_arr(A, k))