def quicksort(nums):
    if len(nums) <= 1:
        return nums
    left = []            # 左数列
    right = []           # 右数列
    base = nums.pop()    # 每次的基准
    # 对数组划分左右数列
    for x in nums:
        if x < base:
            left.append(x)
        else:
            right.append(x)
    # 递归调用下去，直到left和right内元素 <= 1
    return quicksort(left) + [base] + quicksort(right)

if __name__ == '__main__':
    nums = [5, 3, 3, 4, 3, 8, 9, 10, 11]
    print(quicksort(nums))