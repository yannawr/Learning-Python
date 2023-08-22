
def selectionSort(numList):
    
    length = len(numList)
    
    for i in range(length):
        min_index = i
        
        for j in range(i + 1, length):
            if numList[j] < numList[min_index]:
                min_index = j
                
        numList[i], numList[min_index] = numList[min_index], numList[i]

nums = [64, 28, 49, 12, 16, 8, 90]

selectionSort(nums)

print(nums)