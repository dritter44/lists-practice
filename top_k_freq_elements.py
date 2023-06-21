# given an integer array nums, and an integer k, return the k most frequent elements, return in any order

def top_k_freq_elems(nums,k):
    # nums = [1,1,1,2,2,3], k = 2
    # nums = [1], k = 1
    # the elements won't always be in order, so have to map a count of all the values to value in a dicct
    # then sort the array of value
    count_dict = {}
    ans_list = []
    for i in nums:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    # x = count_dict.values()
    # sort count_dict.values
    sort_vals = sorted(count_dict.values())
    print(sort_vals)
    # push kth elements to a mid list

    # threshold is last element in mid list
    thresh = sort_vals[len(sort_vals)-k]
    print(thresh)
    
    # iter through dict, if value of ele is higher than threshold
    for ele in count_dict:
        if count_dict[ele] >= thresh:
            # push ele to ans dict
            ans_list.append(ele)
    

        
    
    return ans_list

top_k_freq_elems([3,0,1,0],1)