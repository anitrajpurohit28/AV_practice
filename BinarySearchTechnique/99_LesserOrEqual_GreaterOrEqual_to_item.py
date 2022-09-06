# Given a sorted array Arr of size N and a value X,
# find the number of array elements
# A. less than or equal to X and
# B. greater than or equal to X
import logging
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def getMore(self, arr, n, item):
        """
        This Function will find the number of elements that are greater then or equal to given item.
        Logic:
            Apply BS on the array such that
            if item is found,
                Store the result in temp element
                keep searching for element towards left, as we may have duplicates
            if item is greater the current mid
                store the result in temp element as this could be potential result
                keep searcihng on right array
            if item is lesser than current mid
                Move towards left array
            final_result = size - temp_result   => In case we find the exact match
            OR
            final_result = size - (temp_result + 1) => If we don't find he exact match
        """
        # Example: [1, 2, 5, 5, 5, 6, 8]; item 5; size = 7
        # more           ^
        # Here we 5 element are greater than or equal to 5;
        # which is result = size - (temp + 1); 7 - (2 + 1)
        # +1 because of index starts from 0
        low = 0
        high = n-1
        result = 0
        while low <= high:
            mid = low + (high-low)//2
            logging.debug('Array: %s; mid=%s; a[mid]=%s', arr[low: (high if high == n else high+1)], mid, arr[mid])
            if arr[mid] == item:
                # the given item is present in the array; Store it in temperory result as this is potential answer
                # We need to keep searching on left as we may have duplicates as well.
                # We need to move towards left as the problem states we need to find items greater or EQUAL TO
                result = mid
                logging.debug('Found the matching element; res_index=%s; Continuing right for more', result)
                high = mid - 1
            elif arr[mid] < item:
                logging.debug('Current a[mid]=%s is lesser and is potential candidate; continuing right for more', arr[mid])
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        logging.debug('## mid: %s; res: %s##', mid, result)

        # By now, we would have the potential solution stored in result
        if arr[result] == item or mid == 0:
            # Explaination 1: (better)
            # if the exact item is found in arr[result], just return "n-result"
            # size - result would have discounted the current element too so, ideally, we should be
            # adding +1 to take account of the current item but we need not do that as the index of
            # array is starting from 0, 1st element of the array is discounted. 1st discounted element
            # will equilizes the current element to be considered.

            # Explaination 2:
            # if the exact item is found in arr[result], just return "n-result" instead of "n-(result+1)"
            # because, current element is equal it item and we must count this too; After doing -1, we'll
            # be pointing to element left of the result,
            # Now we need to discount the element from start to left of result;
            # AND
            # in case the element is lesser than first element, the size of array is the answer; In this case
            # result will be 0; size - 0 = size of array
            final_result = n - result
        else:
            # the reason for "result+1" is because the index starts from 0 and not 1;
            final_result = n - (result+1)
        logging.info('getMore: index from where elements are greater: [%s]; result: [%s]', result, final_result)
        return final_result


    def getLess(self, arr, n, item):
        """
        Find the number of elements lesser or equal to given element
        Logic:
        Apply BS such that;
            if element is found:
                store the mid in temp_result as this is potential solution
                Continue searching on right array as we need to consider till the element that
                    are equal and are on right array
            if item is greater than array[mid]:
                meaning arr[mid] is lesser than item and is potential candidate; store in temp_result
                keep searching on right array for duplicates, if any
            else:
                keep searching on left array
        """
        low = 0
        high = n-1
        result = -1
        while low <= high:
            mid = low + (high-low)//2
            logging.debug('Array: %s; mid=%s; a[mid]=%s', arr[low:(high if high == n else high+1)], mid, arr[mid])
            if item == arr[mid]:
                result = mid
                logging.debug('Found the matching element; res_index=%s; continuing to right', result)
                low = mid+1
            elif arr[mid] < item:
                logging.debug('Current a[mid]=%s is lesser and is potential candidate; continuing left for more', arr[mid])
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        # return result + 1 because index is starting with 0 and not 1
        logging.info('getLess: index from where elements are lesser: [%s];', result+1)
        return result+1

    def getMoreAndLess(self, arr, n, item):
        logging.debug('Array: %s; item = %s', arr, item)
        less = self.getLess(arr, n, item)
        print('-----')
        more = self.getMore(arr, n, item)
        logging.info('Less:[%s], More: [%s]', less, more)
        return less, more



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# arr = [1, 2, 8, 10, 11, 12, 19]
# ob = Solution()
# ob.getMoreAndLess(arr, 7, 0)

# arr = [3, 3, 3]
# ob = Solution()
# ob.getMoreAndLess(arr, 3, 3)
