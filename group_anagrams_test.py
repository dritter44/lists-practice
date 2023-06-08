import unittest
from group_anagrams import group_anagrams

# class TestLeetCodeAnswer(unittest.TestCase):
#     def test_tw_sum(self):
#         nums = [2,7,11,15]
#         target = 9
#         result = one_pass(nums,target)
#         self.assertEqual(result,(0,1))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

class TestLeetCodeAnswer(unittest.TestCase):
    def test_grp_ana(self):
        str_lst = ["eat","tea","tan","ate","nat","bat"]
        result = (group_anagrams(str_lst))
        self.assertEqual(result,[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
