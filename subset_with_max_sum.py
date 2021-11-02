

'''
Given an array of integers and number k, return the highest sum of any k consecutive elements in the array
'''


def highest_sum(arr,k):

    right = left = 0
    max_sum = float('-inf')
    win_max_sum= []
    curr_sum = 0
    curr_win = []
    if k>len(arr):
        return -1

    while right < len(arr):
        curr_sum += arr[right]
        curr_win.append(arr[right])
        right+=1

        if right - left == k :
            if max_sum < curr_sum:
                max_sum = curr_sum
                win_max_sum = curr_win.copy()
            curr_win = curr_win[1:]
            curr_sum -= arr[left]
            left +=1

    return win_max_sum,max_sum


arr =[5, -3, 7, -6, 8]
k = 3
print(highest_sum(arr,k))


