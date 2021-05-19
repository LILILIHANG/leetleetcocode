#快速排序
def quick_sort(alist, start, end):
    if start >= end:
        return

    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        #每一轮循环都要交换两个值，所以整个数组的值不会缺失
        while low<high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= mid_value:
            low += 1
        alist[high] = alist[low]
    #当low 和 high相遇时证明循环结束，将mid的值放到low(high)的位置，此时alist[low（high）]左侧值小，右侧值大
    alist[low] = mid_value
      分别对alist[low]左右的区间再排序
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    quick_sort(li, 0, len(li)-1)
    print(li)

# 堆排序
# 向下调整函数的实现, 此处建立大根堆，可实现数组升序排列
def sift(alist, low, high):
    # 假设只有根节点需要调整，两棵子树都是堆
    i = low
    j = i *2 +1 #j指向i的左子树
    tmp = alist[i]
    while j <=high:
        if j+1<= high and alist[j] < alist[j+1]: #右子树比较大,则指向右子树
            j = j+1
        if alist[j] > tmp:  # 若子树的值比较大，则根节点换成子树，然后向下看一层
            alist[i] = alist[j]
            i = j
            j = i *2 +1
        else:
            alist[i] = tmp # 子树的值小于根节点，则根节点就放在这一层
            break
    else:
        alist[i] = tmp # j越界跳出循环，则把根节点放在叶子节点


def heap_sort(alist):
    # 1、建堆
    # 先找到最后一个不是叶子节点的根节点，为(n-2)//2 (若叶子节点为i，则他的父节点为(i-1)//2 )
    # 再向上循环根节点，从小到大
    n = len(alist)
    for i in range((n-2)//2, -1, -1):
        sift(alist,i,n-1)

    # 2、挨个出数，按升序排列
    for i in range(n-1, -1, -1):
        alist[0], alist[i] = alist[i], alist[0]
        sift(alist, 0, i-1)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    heap_sort(li)
    print(li)
