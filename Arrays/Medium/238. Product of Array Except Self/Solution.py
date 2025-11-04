class Solution:
    #new solution using pre and post products matrix
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        answer = [1]*lenght
        pre = [1]*lenght
        post = [1]*lenght

        product = 1
        for i in range(len(nums)):
            pre[i] = product
            product = product*nums[i]

        product = 1
        for i in range(len(nums)-1, -1, -1):
            post[i] = product
            product = product*nums[i]

        for i in range(len(nums)):
            answer[i] = pre[i]*post[i]

        return answer