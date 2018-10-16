#!/usr/bin/python
#  -*- coding: UTF-8 -*-
# Time: 2018/10/15 15:27

#
# # 1. 插入排序
# def insert_sort(ilist):
#     for i in range(0, len(ilist)):
#         for j in range(i):
#             if ilist[i] < ilist[j]:
#                 ilist.insert(j, ilist.pop(i))
#     return ilist
#
# ilist = insert_sort([2, 3, 4, 7, 9, 8, 5, 6, 10])
# print '插入：', ilist
#
# # 2. 希尔排序
# def shell_sort(slist):
#     gap = len(slist)
#     while gap > 1:
#         gap = gap // 2
#         for i in range(gap, len(slist)):
#             for j in range(i % gap, i, gap):
#                 if slist[i] < slist[j]:
#                     slist[i], slist[j] = slist[j], slist[i]
#     return slist
#
# slist = shell_sort([2, 3, 4, 7, 9, 8, 5, 6, 10])
# print '希尔：', slist
#
# # 3. 冒泡排序
# def bubble_sort(blist):
#     count = len(blist)
#     for i in range(0, count):
#         for j in range(i + 1, count):
#             if blist[i] > blist[j]:
#                 blist[i], blist[j] = blist[j], blist[i]
#     return blist
# blist = bubble_sort([2, 3, 4, 7, 9, 8, 5, 6, 10])
# print '冒泡：', blist
#
#
# # 4. 快速排序  将要排列的数据分成两组，一部分的所有数据都要比林一部分的数据要小
# #              然后再按此方法对这两部分数据分别进行快速排序，整个排序可以进行递归进行。
#  时间复杂度： O(nlog2n)  空间复杂度O(nlog2n)   稳定性：不稳定
#
# def quick_sort(qlist):
#     if qlist == []:
#         return []
#     else:
#         qfirst = qlist[0]
#         qless = quick_sort([l for l in qlist[1:] if l < qfirst])
#         qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
#         return qless + [qfirst] + qmore
# qlist =  quick_sort([2, 3, 4, 7, 9, 8, 5, 6, 10])
# print '快排：', qlist

# 5. 选择排序  选择第一个值，然后从待排序的队列中找出最小的值，
#              将它与第一个交换，然后第二趟找后面待排队列中的最小值，交换位置，以此类推。
#    时间复杂度： O(n^2)          空间复杂度O(1)        稳定性：不稳定
def select_sort(slist):
    for i in range(len(slist)):
        x = i
        for j in range(i + 1, len(slist)):
            if slist[j] < slist[x]:
                x = j
        slist[i], slist[x] = slist[x], slist[i]
    return slist
slist =  select_sort([2, 3, 4, 7, 9, 8, 5, 6, 10])
print '选择：', slist



