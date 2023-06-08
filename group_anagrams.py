# given an array of string, group the anagrams together. you can retunr the answer in any order

# ex: ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]]
# group in an array
# use sorted() to sort the strings
# sorted str are the keys in the dict, the words themselves are the values, pushed to arrays
# then iterate through the dict, appending the values to an answer array
def group_anagrams(strs):
    # initialize dict
    group_dict = {}
    # initilize answer array
    ans_arr = []
    # loop through strs
    for str in strs:
        srtd_str = "".join(sorted(str))
        if srtd_str in group_dict:
            group_dict[srtd_str].append(str)
        else:
            group_dict[srtd_str] = []
            group_dict[srtd_str].append(str)
    
    #iter through dict, appending values to ans array
    for ele in group_dict:
        ans_arr.append(group_dict[ele])
    print(ans_arr)
    return ans_arr

group_anagrams(["eat","tea","tan","ate","nat","bat"])

# leetcode answer
# leetcode makes the count of letters in the individual strings as the keys to map the strings to
#  import default dict
from collections import defaultdict

def def_dict_group_ana(strs):
# uses a default dict with a default value of list: defaultdict(list)
    res = defaultdict(list)
    # loops through list of strings
    for s in strs:
        # initializes the count list (list of the counts of letters a - z)
        count = [0]*26
        # loops through characters in string
        for c in s:
            # upcount the value of the number at the index of the letter; subtracts the unicode of "a" from the unicode char of the letter current letter being iterated
            count[ord(c)-ord("a")] += 1
        # append the word to the key value for that count:
        res(tuple(count)).append(s)
    # return an array of the values of the result defaultdict
    return res.values
# count of letters in strings as keys to default dict: