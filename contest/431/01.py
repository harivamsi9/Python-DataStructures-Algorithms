from typing import List
from math import gcd
from functools import reduce

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def compute_gcd(arr):
            return reduce(gcd, arr)

        def compute_lcm(arr):
            def lcm(a, b):
                return abs(a * b) // gcd(a, b)
            return reduce(lcm, arr, 1)

        maxlen = 0
        n = len(nums)

        for i in range(n):
            subarr = []
            for j in range(i, n):
                subarr.append(nums[j])
                g = compute_gcd(subarr)
                l = compute_lcm(subarr)
                prod = 1
                for num in subarr:
                    prod *= num
                if prod == g * l:
                    maxlen = max(maxlen, j - i + 1)

        return maxlen

# Example usage:
s = Solution()
nums = list(map(int, input("Enter numbers separated by commas: ").split(',')))
print("Maximum Length:", s.maxLength(nums))
