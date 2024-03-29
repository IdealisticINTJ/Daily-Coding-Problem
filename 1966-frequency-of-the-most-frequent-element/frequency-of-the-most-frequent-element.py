class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, left, max_freq, current_sum = len(nums), 0, 0, 0

        for right in range(n):
            current_sum += nums[right]
            while (right - left + 1) * nums[right] - current_sum > k:
                current_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq