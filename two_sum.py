# given an array of integers, and an int target, return the indicies of the two numbers such that they add up to target.
# test case 1: [2,7,11,15],9
# test case 2: [3,2,4], 6
#test case 3: [3,3],6
#test case: where no indicies add up to target: [1,3,4], 10
#test case: multiple indicies add up to target: [2,1,3,2], 4

def two_sum(arr,target):
    # return the indicies of the two values that add up to target
    # brute force:
    # outer loop: iterate through the arr each item:
    for i in range(0,len(arr)):
        # inner loop: iterate through index 1, until end
        for j in range(i+1,len(arr)):
            # condition arr[i] + arr[j] must equal target
            if arr[i]+arr[j] == target:
                return i,j
            
    
    
    return "No matches found"

# higher level solutions
# two pointers solution
def two_sum_pointers(nums,target):
    #return indicies of the arr entries that add up to target
    #need to iterate through the loop continuously
    #need to iterate through loop until front pointer reaches 2nd to last position of the array
    # pointer1 starts at index 0, pointer2 starts at index 1, loop ends at pointer1 at n-1 position
    p1 = 0
    p2 = p1 + 1

def one_pass(nums,target):
    #uses a hashmap
    #initialize hashmap
    hmap = {}
    #iterate through
    for i in range(0,len(nums)):
        if (target - nums[i]) in hmap:
            return hmap[target-nums[i]],i
        hmap[nums[i]] = i
