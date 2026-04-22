# 我的作答
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用

def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    # 要求：
    # 1) 将节点 P 插入到 n0 后面（即 n0 -> P -> 原来的下一个节点）。
    # 2) 需要正确处理指针顺序，避免链表断开。
    # 3) 时间复杂度应为 O(1)。
    P.next = n0.next
    n0.next = P



def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    # 要求：
    # 1) 删除 n0 的下一个节点。
    # 2) 若 n0 后面没有节点，直接返回。
    # 3) 删除后仍保持链表正确连接。
    # 4) 时间复杂度应为 O(1)。
    n1 = n0.next
    if not n1: return
    n2 = n1.next
    n0.next = n2



def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    # 要求：
    # 1) 从头节点开始向后遍历，返回第 index 个节点（0-based）。
    # 2) 若 index 越界（链表长度不足），返回 None。
    # 3) 注意处理 index = 0 的情况。

    # 错误, 没有处理head=None
    # if not index:
    #     return head 
    # now = head
    # while now.next:
    #     now = now.next
    #     index -= 1
    #     if index == 0:
    #         return now.val
    # return None
    if index == 0:
        return head
    while head:
        head = head.next
        index -= 1
        if index == 0:
            return head
    return None


def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    # 要求：
    # 1) 从头节点开始遍历链表。
    # 2) 找到值等于 target 的第一个节点时，返回其索引（0-based）。
    # 3) 若不存在目标值，返回 -1。

    # 错误, head没有往后动, 而且没找到也不返回-1
    # ans = -1
    # while head:
    #     ans += 1
    #     if target == head.val:
    #         break     
    # return ans
    
    ans = 0
    while head:
        if target == head.val:
            return ans
        head = head.next
        ans += 1
    return -1
        
    

'''答案'''
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用

def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P


def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1

def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1