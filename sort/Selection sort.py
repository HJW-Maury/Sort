A = [12, 11, 13, 5, 6, 7, 9, 15]
def SelectionSort(nums):
   for i in range(len(nums)):        # 大循环：第i次扫描(放第i个位置)
       min = i
       for j in range(i + 1, len(nums)):  # 小循环：每次扫描中，不断向后比较，最后确定min的位置
           if nums[min] > nums[j]:
               min = j
       nums[i], nums[min] = nums[min], nums[i]

if __name__ == '__main__':
    SelectionSort(A)
    print("排序后的数组：", A)