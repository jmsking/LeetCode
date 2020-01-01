#! /usr/bin/env python3

"""
给定一个单链表的头节点 head
实现一个调整单链表的函数
使得每K个节点之间为一组进行逆序
并且从链表的尾部开始组起
头部剩余节点数量不够一组的不需要逆序
PS: 不能使用队列或者栈作为辅助
"""

## 普通求解

class LinkNode:
    """
    A link list node definition
    """
    def __init__(self, value):
        self._value = value
        self._next = None
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, v):
        self._value = v
    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, next_node):
        self._next = next_node
    
def sort(linklist, start, end):
    """
    sort the single link list descend from start-node(include) to end-node(include)
    """
    assert (linklist is not None)

    head = linklist

    while head != start:
        head = head.next

    if head.next is None:
        return linklist

    # Using selection sort algorithm
    while head != end:
        p2 = head.next
        max_value = head.value
        while p2:
            if p2.value > max_value:
                max_value = p2.value
                tmp = head.value
                head.value = p2.value
                p2.value = tmp
            p2 = p2.next
            if p2 == end.next:
                break
        head = head.next
    return linklist
        

def build_data(k):
    import random
    head = None
    for _ in range(k):
        node = LinkNode(random.randint(0, 100))
        if head is None:
            head = node
            p = node
        else:
            p.next = node
            p = p.next
    return head

def print_link(linklist):
    head = linklist
    print_str = []
    while head:
        print_str.append(str(head.value))
        head = head.next
    print(' '.join(print_str))
    

def inverseSortForLinkList(linklist, k):
    """
    data : a single link list data
    """

    assert (linklist is not None)
    head = linklist
    size = 0
    while head:
        size += 1
        head = head.next
    if size < k:
        return linklist
    if size == k:
        start = linklist
        end = linklist
        p = linklist
        while p:
            end = p
            p = p.next
        return sort(linklist, start, end)

    head = linklist
    pointers = []
    t = 0
    while head.next:
        if t%k == 0:
            p = linklist
            pointers.append(p)
        pointers = list(map(lambda x:x.next, pointers))
        head = head.next
        t += 1
    p_size = len(pointers)
    for p_idx in range(p_size-1):
        end_p = pointers[p_idx]
        start_p = pointers[p_idx+1].next
        linklist = sort(linklist, start_p, end_p)
        print(f'######## {p_idx} ########')
        print_link(linklist)

    return linklist


if __name__ == '__main__':
    data = build_data(10)
    print_link(data)
    print('#############')
    '''start = data
    end = data
    p = data
    while p:
        end = p
        p = p.next
    sort_data = sort(data, start, end)
    print_link(sort_data)'''
    inverse_data = inverseSortForLinkList(data, 2)
    print_link(inverse_data)