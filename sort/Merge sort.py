# a = b = c = 1
# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # 拷贝数据到临时数组 L[] 和 R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#     # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#     print(arr)
#     print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#
#
# def mergeSort(arr, l, r):
#     global a, b, c
#     if l < r:
#         print('r:', r)
#         print('l:', l)
#         m = int((l + (r - 1)) / 2)   # 画重点，前面那个是字母L的小写！！后面才是数字1！！
#         print('m:', m)
#         print(a, 'aaaaaaaaaaaaaaaaaaaaaaaaaaa')
#         a = a + 1
#         mergeSort(arr, l, m)
#         print(b, 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
#         b = b + 1
#         print('r2:', r)
#         print('m2:', m)
#         print('l2:', l)
#         mergeSort(arr, m + 1, r)
#         print(c, 'cccccccccccccccccccccccccccccc')
#         c = c + 1
#         merge(arr, l, m, r)
#
# if __name__ == '__main__':
#    arr = [12, 11, 13, 5, 6, 7, 9, 15]
#    n = len(arr)
#    mergeSort(arr, 0, n - 1)
#    print("排序后的数组:")
#    print(arr)

# 归并
l = [12, 11, 13, 5, 6, 7, 9, 15]

def merge(left, right):      # 对left和right中元素排序后，覆盖原数组arr上左边(相应位置上)数据
    result = []
    i = j = 0
    while len(left) > i and len(right)>j:
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(l):      # 递归层层挖下去直到len(l) <= 1
    if len(l) <= 1:
        return l
    moddle = int(len(l)/2)
    left = merge_sort(l[0: moddle])      # 先挖左边，再搞右边，然后两边合并一起排序
    right = merge_sort(l[moddle: len(l)])
    print ('left:', left, 'right:', right)
    return merge(left, right)

if __name__ == '__main__':
    a =  merge_sort(l)
    print (a)