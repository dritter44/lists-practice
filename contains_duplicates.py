# given an integer array nums, return true is any value appears at least twice in the array, and return false if every element is distinct

def duplicates(nums):
    #return a helpful hint if input is an empty array
    # if len(nums) < 1:
    #     return "empty string"

    #big picture: iterate through array, map all items to a dict, then if the values of the dict are greater than 1, return false, else return true
    #refinement: if dict key already exists, return false

    #initialize dict
    ans_dict = {}

    #start for loop with iterator
    for num in nums:
        if num in ans_dict:
            ans_dict[num] += 1
            return True
        else:
            ans_dict[num] = 1
    return False

# fast solution: A set is an unordered collection of unique elements. By converting the given list into a set, we can remove all duplicates. If the length of the set is less than the length of the list, it means that there were duplicates in the original list.
#   class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:

    #     return len(set(nums)) < len(nums)