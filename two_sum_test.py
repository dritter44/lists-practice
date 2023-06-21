from two_sum import one_pass
import unittest
# test case 1: [2,7,11,15],9
# test case 2: [3,2,4], 6
#test case 3: [3,3],6
#test case: where no indicies add up to target: [1,3,4], 10
#test case: multiple indicies add up to target: [2,1,3,2], 4
# def main():
#     #point of this is to not repeat myself (dry principle)
#     # array of test arrays
#     test_arr = [
#         [2,7,11,15],
#         [3,2,4],
#         [3,3],
#         [1,3,4],
#         [2,1,3,2]
#     ]
#     # array of test targets
#     test_targ_arr = [9,6,6,10,4]
#     for i in range(0,len(test_arr)):
#         print(f"indicies of {test_arr[i]} that add up to {test_targ_arr[i]} are the following: " + str(two_sum(test_arr[i],test_targ_arr[i])))
class TestLeetCodeAnswer(unittest.TestCase):
    def test_tw_sum(self):
        nums = [2,7,11,15]
        target = 9
        result = one_pass(nums,target)
        self.assertEqual(result,(0,1))

