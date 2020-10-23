def is_circul(head):
    #找到相遇点
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    #找到入环点
    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow