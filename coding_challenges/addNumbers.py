"""
Leetcode #2: Add Numbers
https://leetcode.com/problems/add-two-numbers
Add 2 numbers represented in reverse order as Singly Linked Lists
"""

class ListNode:
     def __init__(self, x):
         self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    head = l1
    carryOn = (l1.val+l2.val) // 10;
    l1.val = (l1.val+l2.val) % 10;
    while l1.next != None and l2.next !=None:
        carryOn += l1.next.val
        carryOn += l2.next.val
        l1.next.val = carryOn % 10
        carryOn = carryOn // 10;
        l1 = l1.next;
        l2 = l2.next;
    if l1.next == None:
        l1.next = l2.next
    while l1.next != None:
        carryOn += l1.next.val
        l1.next.val = carryOn % 10
        carryOn = carryOn // 10;
        l1 = l1.next;
    if carryOn > 0:
        l1.next = ListNode(carryOn)
    return head
