"""
This function simply merges 2 linked lists
and returns the NEW list

runtime and memory usage: O(len(list1) + len(list2))

SinglyLinkedList:
    SinglyLinkedListNode head
    SinglyLinkedListNode tail

 SinglyLinkedListNode:
     int data
     SinglyLinkedListNode next

author: Manish Suthar
"""
def mergeLists(head1, head2):
    l = SinglyLinkedList()
    h = head2
    if head1.data <= head2.data:
        h = head1
        head1 = head1.next
    else:
        head2 = head2.next
    l.head = h

    while head1 and head2:
        new = None
        if head1.data <= head2.data:
            new = head1
            head1 = head1.next
        else:
            new = head2
            head2 = head2.next
        h.next = new
        h = h.next

    if head1:
        h.next = head1
    if head2:
        h.next = head2
    return l.head
