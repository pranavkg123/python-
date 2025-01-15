# -*- coding: utf-8 -*-
"""max_subarray.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M1_-KVLiYi4zvH9BgwKsI5ln_EcDoUll
"""

def max_subarray_sum(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))