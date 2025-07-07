class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # Step 1: Find the middle of the list (use slow and fast pointers)
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    def reverse_list(node):
        prev = None
        curr = node

        while curr:
            curr.next = prev
            prev = curr
            curr = curr.next
        return prev

    second_half = reverse_list(slow)

    # Step 3: Compare the first and second halves
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
