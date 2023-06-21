# given an integer array nums, return an array answer, such that answer[i] is equal to the product of all elements in nums except nums[i]. O(n) time w/o using division operator

# nums = [1,2,3,4]
# [24,12,8,6]

# [-1,1,0,-3,3]
# [0,0,9,0,0]

def product_arr_ex_self(nums):
    # create output arr
    ans_arr = []
    # initialize prefix at 1, need to be able to multiply all nums by it and not have it equal zero
    prefix = 1
    # initialize postfix
    postfix = 1
    #iterate through nums
    for i in range(len(nums)):
        ans_arr.append(prefix)
        prefix *= nums[i]
    
    for y in range(len(nums)-1,-1, -1):
        print(ans_arr[y])
        ans_arr[y] *= postfix
        postfix *= nums[y]

    return ans_arr
product_arr_ex_self([1,2,3,4])