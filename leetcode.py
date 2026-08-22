# def mysqrt(x):
#     left = 1
#     right = 10
#     answer = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if mid * mid <= x:
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#     if answer < 0:
#         print(0)
#     # print(answer)
#     return answer
# mysqrt(0)

# def findPeakElement(nums):
#     left = 1
#     right = len(nums) - 1
#     while left < right:
#         mid = (left + right) //2
#         if nums[mid] < nums[mid + 1]:
#             left = mid + 1
#         else:
#             right = mid
#     print(left)
#     return left
# findPeakElement([1,1,1,1])

# def containsDuplicate(nums):
#     while True:
#         left = nums[0]
#         right = len(nums) - 1
#         if left == nums[right]:
#             print(True)
#             return True
#         else:
#             print(False)
#             return False

# containsDuplicate([1,2,3,1])
# nums = [1,2,3,4,4]
# for i in nums:
# for j in nums:
    