def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]                # 抽出的元素
        j = i - 1
        while j >= 0 and key < arr[j]:     # 不断与前面元素比较
            arr[j + 1] = arr[j]      # 比它大的往后移一个位
            j -= 1
        arr[j + 1] = key             # 直到有元素比它小，则该元素不用往后移，它插入中间这个空位上

if __name__ == '__main__':
   arr = [12, 11, 13, 5, 6, 7, 9, 15]
   insertionSort(arr)
   print("排序后的数组:", arr)