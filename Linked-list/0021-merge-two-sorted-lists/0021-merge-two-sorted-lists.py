
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node to simplify merging
        dummy = ListNode()

        # Tail always points to the last node in the merged list
        tail = dummy

        # Compare nodes from both lists
        while list1 and list2:

            # Attach the smaller node to the merged list
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move the tail forward
            tail = tail.next

        # Attach the remaining nodes
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return the merged list (skip the dummy node)
        return dummy.next