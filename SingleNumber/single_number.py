from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while (i+1)<len(nums):
            if nums[i] != nums[i+1]:
                break
            i += 2
        return nums[i]


if __name__ == "__main__":
    cases = [
        {
            "nums": [2,2,1],
            "result": 1
        },
        {
            "nums": [4,1,2,1,2],
            "result": 4
        },
        {
            "nums": [1],
            "result": 1
        }
    ]

    for case in cases:
        result = Solution().singleNumber(case["nums"])
        print("result", result)
        assert result == case["result"]