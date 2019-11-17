def BucketSort(s):
    min_num = min(s)
    max_num = max(s)
    # 桶的大小
    bucket_range = (max_num-min_num) / len(s)
    # 桶数组(二维，行是各个桶，列是桶的深度)
    count_list = [[] for i in range(len(s) + 1)]
    # 向桶数组填数
    for i in s:
        count_list[int((i-min_num)//bucket_range)].append(i)
    s.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            s.append(j)

if __name__ == '__main__':
    a = [12, 11.2, 11.3, 5, 6, 7, 9, 9, 15]
    BucketSort(a)
    print(a)