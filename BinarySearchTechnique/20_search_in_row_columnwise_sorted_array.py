import logging
logging.basicConfig(level=logging.INFO)

def search_in_row_columnwise_sorted_array(arr, item):
    """ Search for an element in 2D row wise sorted and column wise
        sorted array
        Logic:
            Start from top right corner. If the current element is the
            item to be searched for is current item,
                return the row, column index
            If current element(i, j) is greater than item,
                move left of column index
            If current element(i, j) is lesser then item,
                move down of row index
    """
    col_len = len(arr[0])
    row_len = len(arr)
    if logging.getLevelName(logging.getLogger().level) == "DEBUG":
        print('Input array: ')
        for i in range(row_len):
            for j in range(col_len):
                print(f'{arr[i][j]}', end=' ')
            print()
    logging.debug('Item to search for: %s', item)
    logging.debug('row len: %s; col len: %s', row_len, col_len)

    row_index = 0
    col_index = col_len -1

    while row_index < row_len and col_index >= 0:
        logging.debug('curent index: (%s,%s); element: %s',
                        row_index,
                        col_index,
                        arr[row_index][col_index])
        if arr[row_index][col_index] == item:
            logging.info('Item found at index: (%s,%s)', row_index, col_index)
            return (row_index, col_index)
        if arr[row_index][col_index] < item:
            row_index += 1
        else:
            col_index -= 1

    logging.info('Item not found')
    return -1

array = [[10, 20, 30, 40],
         [15, 25, 35, 45],
         [27, 29, 37, 48],
         [29, 31, 38, 49],
         [32, 33, 39, 50]]

res = search_in_row_columnwise_sorted_array(array, 29)
print(res)
res = search_in_row_columnwise_sorted_array(array, 40)
print(res)
res = search_in_row_columnwise_sorted_array(array, 32)
print(res)
res = search_in_row_columnwise_sorted_array(array, 10)
print(res)
res = search_in_row_columnwise_sorted_array(array, 50)
print(res)
res = search_in_row_columnwise_sorted_array(array, 34)
print(res)




# ======GFG solution ========
# class Solution:
#     def matSearch(self,arr, N, M, item):
#         # Complete this function
#         col_len = M
#         row_len = N

#         row_index = 0
#         col_index = col_len -1

#         while row_index < row_len and col_index >= 0:
#             if arr[row_index][col_index] == item:
#                 return 1
#             if arr[row_index][col_index] < item:
#                 row_index += 1
#             else:
#                 col_index -= 1
#         return 0


# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n, m = tuple(map(int, input().split()))
#         arr = [int(x) for x in input().split()]
#         x = int(input())
#         mat = [[0 for j in range(m)] for i in range(n)]

#         for i in range(n):
#             for j in range(m):
#                 mat[i][j] = arr[i*m+j]
#         ob = Solution()
#         print(ob.matSearch(mat, n, m, x))