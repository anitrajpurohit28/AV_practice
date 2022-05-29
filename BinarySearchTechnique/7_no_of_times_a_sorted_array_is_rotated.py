# Number of times a sorted array is rotated

# 1. index of minimum element is equal to number of times array is rotated.
#    start ....... mid ........ end;
# 2. if start <= mid: left part of array is sorted
# 3. if mid <= end: right part of array is sorted
# 4. Minimum element if always found in unsorted part of array

class Solution:
    def no_of_times_a_sorted_array_is_rotated(self, arr, n):
        print(arr)
        low = 0
        high = len(arr) -1
        arr_length = len(arr)
        # if array is already in sorted order, return 0 as it is not rotated.
        if arr[low] <= arr[high]:
            return 0
        while low <= high:
            mid = low + (high - low)//2
            # mid+1 and mid-1 could lead to "IndexError: list index out of range"
            next = (mid + 1) % arr_length
            prev = (mid + arr_length - 1) % arr_length
            if debugging:
                print(f'mid: {mid}; next: {next}; prev: {prev};')
                print(f'mid: {arr[mid]}; next: {arr[next]}; prev: {arr[prev]};')
                print(prev >= arr[mid], arr[mid] <= next)
                print()
            if arr[prev] >= arr[mid] <= arr[next]:
                #return mid, arr[mid]  # This is what we are looking for
                return f'index: {mid}; item: {arr[mid]}'  # This is for more readibility
            # if low < mid, left arrary is sorted already; search in right array
            if arr[0] <= arr[mid]:
                low = mid + 1
            else:  # arr[arr_length - 1] >= arr[mid]: right array is sorted; search in left array
                high = mid -1

debugging = False
ob = Solution()
arr1 = [6, 7, 8, 9, 1, 2]
result = ob.no_of_times_a_sorted_array_is_rotated(arr1, 'dummy')
print(result)


arr2 = [23, 34, 56, 77, 88, 20]
result = ob.no_of_times_a_sorted_array_is_rotated(arr2, 'dummy')
print(result)

arr3 = [23, 34, 56, 77, 88, 99]
result = ob.no_of_times_a_sorted_array_is_rotated(arr3, 'dummy')
print(result)


if __name__ == '__main__':
    debugging = True
    tc = int(input())
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.no_of_times_a_sorted_array_is_rotated(a, n)
        print(ans)
        tc = tc - 1
