class Solution:
    #new solution using pre and post products arrays and O(1) space complexity by operating inside of the array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        answer = [1]*lenght
        pre = 1
        post = 1

        for i in range(len(nums)):
            answer[i] = pre
            pre = pre*nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i]*post
            post = post*nums[i]

        return answer