def CountSort(nums):
    list = [0] * (max(nums) - min(nums) + 1)   # 初始化一个计数表
    t = min(nums)
    for i in nums:
        list[i - t] = list[i - t] + 1                # 统计出现次数
    i = j = 0
    while(j < len(list)):             # 把出现次数>1的，依次覆盖原数组
        if(list[j] > 0):
            nums[i] = j + t
            i = i + 1
            list[j] = list[j] - 1   # 覆盖一次后，记得列表里数目-1(相当于被拿走了)
        else:
            j = j + 1

if __name__ == '__main__':
   arr = [12, 11, 13, 5, 6, 7, 9, 9, 15]
   CountSort(arr)
   print("排序后的数组:", arr)