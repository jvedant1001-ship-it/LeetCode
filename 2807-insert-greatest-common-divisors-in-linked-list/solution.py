class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head

        while curr and curr.next:
            a = curr.val
            b = curr.next.val

            # Calculate GCD using Euclidean algorithm
            while b:
                a, b = b, a % b

            # Create and insert new node
            new_node = ListNode(a)
            new_node.next = curr.next
            curr.next = new_node

            # Move to the original next node
            curr = new_node.next

        return head
