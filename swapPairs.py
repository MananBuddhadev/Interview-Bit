class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def swapPairs(self, A):
    if A == None or A.next == None:
        return A
    dummy = ListNode(0);
    dummy.next = A
    p = dummy
    while p.next and p.next.next:
        tmp = p.next.next
        p.next.next = tmp.next
        tmp.next = p.next
        p.next = tmp
        p = p.next.next
    return dummy.next