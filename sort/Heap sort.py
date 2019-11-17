def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # 根据二叉树公式知，i节点的两子节点是left=2*i+1，right=2*i+2
    r = 2 * i + 2  # 注意：这里的最高节点是0节点！
    if l < n and arr[i] < arr[l]:  # 配合调用时的i递减，找到最小的父节点，并确定其下两子节点谁最大
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 把最大子节点和父节点交换，确保了父节点大于两子节点
        heapify(arr, n, largest)  # 向左走横扫该层其他节点，若有父节点则立刻执行这个实现交换

def heapSort(arr):
    n = len(arr)
    # 建一个大根堆
    for i in range(n, -1, -1):  # 注意i是n到0
        heapify(arr, n, i)
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 最高和最下交换,注意变化的是最下位置。
        print(arr)
        heapify(arr, i, 0)

if __name__ == '__main__':
    arr = [12, 11.2, 11.3, 5, 6, 7, 9, 9, 15]
    print("排序前额数组：", arr)
    heapSort(arr)
    print("排序后的数组：", arr)