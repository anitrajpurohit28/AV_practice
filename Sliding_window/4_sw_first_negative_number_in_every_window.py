# 1st Negative number in every window of size K

# arr: Input array
# k: Window size


"""
Fixed window size:
------------------
i = 0
j = 0
while j < len(arr):
    #do calculations
    if current_window_size < K:  # < current_window_size = j-i+1; k = given window size
        j++
    if current_window_size == k  :# < current_window_size = j-i+1;
        # answer <- computation
        # remove i from calculations
        # slide the window; window size is maintained

return the answer
"""

def first_negative_number(arr: list, k: int):
    """
    Logic is to have i and j point to the two ends of the
    window and store the list of negative elements between them, in order.
    For every iteration,
        if item is negative:
            append the item in negative_array list
        if window_size is not K:
            just increase the window size by j++
        else:
            if no elements in negative array:
                append 0 to output
            else:
                append 1st number to output_list
                if negative_list[i] is arr[i]: (arr[i] 1st element which will be out of window)
                    pop the element from negative array as
                    This element will not be part next window
            i += 1
            j+= 1

    Note: This will also work for the duplicate negative numbers as
    all the negative numbers are stored in the negative_numbers list
    and windows 1st negative number is always stored as 1st number in
    negative number list
    """
    i = 0
    j = 0
    negative_numbers = []  # to store the list of negative numbers
    output_list = []  # to store the output
    # We must process only till we hit the end of array
    while j < len(arr):
        # If the element is negative, append it in negative list
        if arr[j] < 0:
            negative_numbers.append(arr[j])
        # if the window size is not yet met, just increase the right
        # edge of the window
        if j-i+1 < k:
            j += 1
        else:  # j-i+1 == k:
            # case where there are no negative numbers in the current window,
            # we must append 0 to the output
            if len(negative_numbers) == 0:
                output_list.append(0)
            else:
                # Negative numbers are present in this window. 1st number will
                # be stored as 1st element in the negative list. Append it to the
                # output
                output_list.append(negative_numbers[0])

                # Before sliding the window to the right, check if the 1st element
                # of the window is same as 1st number in negative number list. If so,
                # pop the number from the negative number list
                if arr[i] == negative_numbers[0]:
                    negative_numbers.pop(0)
            #Slide the window towards right
            i += 1
            j += 1
    # return the output
    return output_list

input_arr = [3, 5, -1, -1, 4, -2, 9, 6, 1, -9, 2]
res = first_negative_number(input_arr, 3)
print(res)


input_arr = [3, 5, 4, 9, 0, 0, -2]
res = first_negative_number(input_arr, 3)
print(res)
