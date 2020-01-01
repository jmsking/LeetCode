#! /usr/bin/env python3

"""
给定一个单链表的头节点 head
实现一个调整单链表的函数
使得每K个节点之间为一组进行逆序
并且从链表的尾部开始组起
头部剩余节点数量不够一组的不需要逆序
PS: 不能使用队列或者栈作为辅助
"""

## 递归求解

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

def sort(linklist):
    """
    sort the single link list descend
    """
    assert (linklist is not None)

    head = linklist
    # Using selection sort algorithm
    while head.next:
        p2 = head.next
        min_value = head.value
        while p2:
            if p2.value < min_value:
                min_value = p2.value
                tmp = head.value
                head.value = p2.value
                p2.value = tmp
            p2 = p2.next
        head = head.next
    return linklist 

def sortKGroup(linklist, k):
    if linklist is None:
        return None

    head = linklist
    size = 0
    while head:
        head = head.next
        size += 1
    if size < k:
        return linklist

    first_head = linklist
    p = first_head
    t = 1
    while p and t < k:
        p = p.next
        t += 1

    second_head = p.next
    p.next = None
    head = sort(first_head)
    remain_head = sortKGroup(second_head, k)
    end_node = head
    while end_node.next:
        end_node = end_node.next
    end_node.next = remain_head
    return head

def reverseLinkList(linklist):
    tail_node = None
    next_node = None
    head = linklist
    while head:
        next_node = head.next
        head.next = tail_node
        tail_node = head
        head = next_node
    return tail_node
        
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
    
    head = reverseLinkList(head)
    print_link(head)
    head = sortKGroup(head, k)
    print_link(head)
    head = reverseLinkList(head)

    return head


if __name__ == '__main__':
    data = build_data(10)
    print_link(data)
    print('#############')
    #sort_data = sort(data)
    #print_link(sort_data)
    #reverse_linklist = reverseLinkList(data)
    #print_link(reverse_linklist)
    inverse_data = inverseSortForLinkList(data, 3)
    print_link(inverse_data)