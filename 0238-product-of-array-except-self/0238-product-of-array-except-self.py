class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Initialize the answer array with 1s
        answer = [1] * length
        
        # Calculate the left prefix product for each element
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # Calculate the right suffix product for each element
        right = 1
        for i in range(length - 1, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]
        
        return answer