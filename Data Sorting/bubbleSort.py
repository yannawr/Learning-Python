def bubbleSort(numList):
    length = len(numList)
    for i in range(length):
        for j in range(i + 1, length):
            firstNum = numList[i]
            secondNum = numList[j]

            if firstNum > secondNum:
                nums[i], nums[j] = nums[j], nums[i]


nums = [64, 28, 49, 12, 16, 8, 90]

bubbleSort(nums)

print(nums)