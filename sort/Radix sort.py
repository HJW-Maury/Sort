def RadixSort(a):
    n = 1                               # 最小的位数为1
    max_num = max(a)                    # 数组中最大数
    while max_num > 10**n:              # 计算最大数是几位数
        n += 1
    for i in range(n):
        bucket = {}             # 用字典构建桶,因为字典可以一个键对应多个值，每个键的值数目可以不同
        for x in range(10):
            bucket.setdefault(x, [])    # 设置一键(0~9)对应一桶，将每个桶置空
        for x in a:                     # 按第i位的基数排序每个元素
            radix = int((x / (10**i)) % 10)   # 计算每位的基数
            bucket[radix].append(x)           # 将对应的元素复制入相应的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:       # 若桶不为空
                for y in bucket[k]:         # 将该桶中每个元素，依次覆盖到原数组
                    a[j] = y
                    j += 1

if  __name__ == '__main__':
    a = [12, 11, 13, 5, 6, 7, 9, 9, 15]
    RadixSort(a)
    print(a)