def twoSum(nums, target):
    numsDict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in numsDict:
            return[i, numsDict[diff]]
        else:
            numsDict[nums[i]] = i